import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

# Function to insert weekly schedules
def insert_schedule(schedule_type, schedule_data):
    for day, meals in schedule_data.items():
        cursor.execute("""
        INSERT INTO weekly_schedule (schedule_type, day, breakfast, lunch, snack, dinner) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (schedule_type, day, meals["breakfast"], meals["lunch"], meals["snack"], meals["dinner"]))
    conn.commit()

# Proper Non-Veg Weekly Schedules
nonveg_schedule_1 = {
    "Monday":    {"breakfast": "Omelette with Toast", "lunch": "Chicken Curry with Rice", "snack": "Chicken Samosa", "dinner": "Grilled Fish with Vegetables"},
    "Tuesday":   {"breakfast": "Scrambled Eggs with Roti", "lunch": "Mutton Keema with Paratha", "snack": "Egg Roll", "dinner": "Butter Chicken with Naan"},
    "Wednesday": {"breakfast": "Chicken Sandwich", "lunch": "Fish Fry with Jeera Rice", "snack": "Chicken Nuggets", "dinner": "Spicy Chicken Wings"},
    "Thursday":  {"breakfast": "Boiled Eggs with Salad", "lunch": "Chicken Biryani with Raita", "snack": "Chicken Pakora", "dinner": "Mutton Rogan Josh with Rice"},
    "Friday":    {"breakfast": "Egg Paratha", "lunch": "Prawn Masala with Chapati", "snack": "Fish Cutlet", "dinner": "Tandoori Chicken with Roti"},
    "Saturday":  {"breakfast": "Chicken Poha", "lunch": "Chicken Korma with Rice", "snack": "Seekh Kebab", "dinner": "Egg Curry with Jeera Rice"},
    "Sunday":    {"breakfast": "Mutton Soup with Bread", "lunch": "Fish Curry with Rice", "snack": "Chicken Tikka", "dinner": "Mutton Biryani with Raita"}
}

nonveg_schedule_2 = {
    "Monday":    {"breakfast": "Chicken Sausage with Eggs", "lunch": "Butter Chicken with Rice", "snack": "Mutton Kebab", "dinner": "Grilled Fish with Lemon Rice"},
    "Tuesday":   {"breakfast": "Scrambled Egg with Toast", "lunch": "Chicken Handi with Chapati", "snack": "Egg Pakora", "dinner": "Prawn Curry with Rice"},
    "Wednesday": {"breakfast": "Egg Bhurji with Paratha", "lunch": "Fish Fry with Dal Rice", "snack": "Chicken Momos", "dinner": "Chicken Masala with Roti"},
    "Thursday":  {"breakfast": "Mutton Keema Toast", "lunch": "Chicken Pulao with Raita", "snack": "Chicken Popcorn", "dinner": "Chicken Do Pyaza with Naan"},
    "Friday":    {"breakfast": "Omelette with Veggies", "lunch": "Mutton Biryani with Raita", "snack": "Fish Fingers", "dinner": "Tandoori Fish with Rice"},
    "Saturday":  {"breakfast": "Chicken Frankie", "lunch": "Egg Curry with Rice", "snack": "Chicken Cutlet", "dinner": "Mutton Keema with Roti"},
    "Sunday":    {"breakfast": "Chicken Soup with Bread", "lunch": "Fish Masala with Jeera Rice", "snack": "Egg Bhurji Roll", "dinner": "Chicken Bhuna with Naan"}
}

nonveg_schedule_3 = {
    "Monday":    {"breakfast": "Mutton Kheema with Toast", "lunch": "Chicken Korma with Roti", "snack": "Chicken Nuggets", "dinner": "Fish Curry with Basmati Rice"},
    "Tuesday":   {"breakfast": "Chicken Salad Sandwich", "lunch": "Butter Garlic Prawns with Rice", "snack": "Chicken Roll", "dinner": "Mutton Rogan Josh with Naan"},
    "Wednesday": {"breakfast": "Omelette with Paratha", "lunch": "Fish Tikka with Lemon Rice", "snack": "Chicken Burger", "dinner": "Chicken Changezi with Roti"},
    "Thursday":  {"breakfast": "Chicken Omelette", "lunch": "Chicken Curry with Roti", "snack": "Egg Puff", "dinner": "Mutton Kadai with Paratha"},
    "Friday":    {"breakfast": "Egg Toast with Avocado", "lunch": "Prawn Biryani with Raita", "snack": "Mutton Seekh", "dinner": "Grilled Chicken with Salad"}
}

# Insert Non-Veg schedules
insert_schedule("nonveg", nonveg_schedule_1)
insert_schedule("nonveg", nonveg_schedule_2)
insert_schedule("nonveg", nonveg_schedule_3)

# Close database connection
conn.close()

print("✅ Non-Vegetarian schedules inserted successfully!")
