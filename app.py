import sqlite3
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from waitress import serve

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

# ✅ Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect("recipes.db")
    conn.row_factory = sqlite3.Row  # Enables column access by name
    return conn

# ✅ Function to fetch a random weekly schedule based on type
def get_random_schedule(schedule_type):
    """Fetch one random weekly schedule of the given type."""
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()

    # Fetch all unique schedule IDs for the given type
    cursor.execute("""
        SELECT DISTINCT id FROM weekly_schedule WHERE schedule_type = ?
    """, (schedule_type,))
    
    schedules = cursor.fetchall()
    conn.close()

    if not schedules:
        return None  # No schedules found

    # Select a random schedule ID
    random_schedule_id = random.choice(schedules)[0]

    # Fetch the weekly schedule for that ID
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT day, breakfast, lunch, snack, dinner 
        FROM weekly_schedule 
        WHERE schedule_type = ? AND id = ?
    """, (schedule_type, random_schedule_id))

    weekly_schedule = cursor.fetchall()
    conn.close()

    # Format the response
    result = {
        "schedule_type": schedule_type,
        "weekly_meals": [
            {
                "day": row[0],
                "breakfast": row[1],
                "lunch": row[2],
                "snack": row[3],
                "dinner": row[4]
            }
            for row in weekly_schedule
        ]
    }
    
    return result

# ✅ API to fetch a random weekly schedule
@app.route("/weekly-schedule", methods=["GET"])
def get_weekly_schedule():
    try:
        schedule_type = request.args.get("type", "").strip().lower()

        if schedule_type not in ["veg", "nonveg", "mixed"]:
            return jsonify({"error": "Invalid schedule type. Use 'veg', 'nonveg', or 'mixed'."}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch schedule based on type
        cursor.execute("""
            SELECT day, breakfast, lunch, snack, dinner FROM weekly_schedule 
            WHERE schedule_type = ? ORDER BY 
                CASE day 
                    WHEN 'Monday' THEN 1
                    WHEN 'Tuesday' THEN 2
                    WHEN 'Wednesday' THEN 3
                    WHEN 'Thursday' THEN 4
                    WHEN 'Friday' THEN 5
                    WHEN 'Saturday' THEN 6
                    WHEN 'Sunday' THEN 7
                END
        """, (schedule_type,))

        schedule = cursor.fetchall()
        conn.close()

        if not schedule:
            return jsonify({"response": "No weekly schedule found for the selected type."})

        weekly_plan = {}
        for row in schedule:
            weekly_plan[row["day"]] = {
                "breakfast": row["breakfast"],
                "lunch": row["lunch"],
                "snack": row["snack"],
                "dinner": row["dinner"]
            }

        return jsonify({"weekly_schedule": weekly_plan})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

# ✅ Search for recipes by name
@app.route("/search", methods=["GET"])
def search_recipes():
    try:
        recipe_name = request.args.get("name", "").strip().lower()

        if not recipe_name:
            return jsonify({"error": "Please provide a recipe name."}), 400

        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        
        # Search for recipes where the name contains the search query
        cursor.execute("SELECT name, ingredients, instructions FROM recipes WHERE LOWER(name) LIKE ?", (f"%{recipe_name}%",))
        recipes = cursor.fetchall()
        conn.close()

        if not recipes:
            return jsonify({"recipes": []})  # Return an empty list instead of an error

        return jsonify({"recipes": [
            {"name": r[0], "ingredients": r[1], "description": r[2]} for r in recipes
        ]})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

# ✅ Get all recipes from the database
def get_recipes_from_db():
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, ingredients, instructions FROM recipes")
    recipes = cursor.fetchall()
    conn.close()
    return [{"name": r[0], "ingredients": r[1], "description": r[2]} for r in recipes]

# ✅ Function to check for harmful ingredient combinations
def check_harmful_combinations(user_ingredients):
    conn = sqlite3.connect("recipes.db")
    cursor = conn.cursor()
    warnings = []
    
    for ingredient in user_ingredients:
        cursor.execute("SELECT ingredient2, message FROM harmful_combinations WHERE LOWER(ingredient1) = ?", (ingredient,))
        results = cursor.fetchall()
        for res in results:
            if res[0] in user_ingredients:
                warnings.append(f"⚠️ {res[1]}")
    
    conn.close()
    return warnings

# ✅ API to fetch recipes based on ingredients
@app.route("/get_recipes", methods=["POST"])
def get_recipes():
    try:
        data = request.get_json()
        if not data or "ingredients" not in data:
            return jsonify({"error": "Invalid request"}), 400
        
        user_ingredients = set(i.strip().lower() for i in data["ingredients"].split(",") if i.strip())

        harmful_messages = check_harmful_combinations(user_ingredients)

        # ✅ Fetch recipes from SQLite database
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, ingredients, instructions FROM recipes")
        recipes = cursor.fetchall()  # List of tuples (name, ingredients, instructions)

        matched_recipes = []
        partial_recipes = []

        min_match_count = 1 if len(user_ingredients) <= 2 else 2

        for recipe in recipes:
            name, ingredients, instructions = recipe
            recipe_ingredients = set(i.strip().lower() for i in ingredients.split(","))

            matched_count = len(user_ingredients & recipe_ingredients)

            if matched_count >= min_match_count:
                missing_ingredients = recipe_ingredients - user_ingredients
                extra_ingredients = user_ingredients - recipe_ingredients

                if not missing_ingredients:
                    matched_recipes.append({
                        "name": name,
                        "description": instructions if instructions else "No instructions available.",
                        "match_count": matched_count
                    })
                else:
                    missing_str = ", ".join(missing_ingredients)
                    extra_str = ", ".join(extra_ingredients) if extra_ingredients else None
                    description = f"You need additional ingredients such as: {missing_str} etc. to make this recipe."
                    if extra_str:
                        description += f"\n❌ Note: {extra_str} etc. are not needed for this recipe."

                    partial_recipes.append({
                        "name": name,
                        "description": description,
                        "match_count": matched_count
                    })

        matched_recipes.sort(key=lambda r: r["match_count"], reverse=True)
        partial_recipes.sort(key=lambda r: r["match_count"], reverse=True)

        all_recipes = matched_recipes + partial_recipes

        if not all_recipes:
            return jsonify({"response": "❌ Sorry, no matching recipes found with the given ingredients."})

        response = ""
        for idx, recipe in enumerate(all_recipes, 1):
            response += f"**Recipe {idx}: {recipe['name']}**\n{recipe['description']}\n\n"

        if harmful_messages:
            response = "\n".join(harmful_messages) + "\n\n" + response

        response += "**🍽️ HAPPY COOKING !! 🎉**"

        return jsonify({"response": response})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

# ✅ API to fetch a **random** recipe (Now includes ingredients)
@app.route("/random-recipe", methods=["GET"])
def random_recipe():
    try:
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, ingredients, instructions FROM recipes ORDER BY RANDOM() LIMIT 1;")  # ✅ Fixed column name
        recipe = cursor.fetchone()
        conn.close()

        if recipe:
            return jsonify({
                "response": f"🍽️ **Recipe:** {recipe[0]}\n📝 **Ingredients Required:** {recipe[1]}\n📖 **Description:** {recipe[2]}\n\n**HAPPY COOKING !!** 🎉"
            })
        else:
            return jsonify({"response": "❌ No recipes found in the database."})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": "Internal Server Error"}), 500

# ✅ API to fetch **three random recipes** (Now includes ingredients)
@app.route("/three-random-recipes", methods=["GET"])
def three_random_recipes():
    try:
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, ingredients, instructions FROM recipes ORDER BY RANDOM() LIMIT 3;")  # ✅ Fixed column name
        recipes = cursor.fetchall()
        conn.close()

        if recipes:
            response = ""
            for idx, recipe in enumerate(recipes, 1):
                response += f"🔥 **Recipe {idx}: {recipe[0]}**\n📝 **Ingredients Required:** {recipe[1]}\n📖 **Description:** {recipe[2]}\n\n"

            response += "**🍽️ HAPPY COOKING !! 🎉**"
            return jsonify({"response": response})
        else:
            return jsonify({"response": "❌ No recipes found in the database."})

    except Exception as e:
        print("Error fetching random recipes:", str(e))
        return jsonify({"response": "❌ Error fetching random recipes."})

# ✅ API to fetch **trending recipes** based on popularity
@app.route("/trending-recipes", methods=["GET"])
def trending_recipes():
    try:
        conn = sqlite3.connect("recipes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, ingredients, instructions FROM recipes ORDER BY popularity DESC LIMIT 3;")  # ✅ Sorting by popularity
        recipes = cursor.fetchall()
        conn.close()

        if recipes:
            response = "**🔥 Trending Recipes:**\n\n"
            for idx, recipe in enumerate(recipes, 1):
                response += f"⭐ **Recipe {idx}: {recipe[0]}**\n📝 **Ingredients Required:** {recipe[1]}\n📖 **Description:** {recipe[2]}\n\n"

            response += "**🍽️ HAPPY COOKING !! 🎉**"
            return jsonify({"response": response})
        else:
            return jsonify({"response": "❌ No trending recipes found in the database."})

    except Exception as e:
        print("Error fetching trending recipes:", str(e))
        return jsonify({"response": "❌ Error fetching trending recipes."})

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)  # Use Waitress for production
