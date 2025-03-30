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

# Mixed Weekly Schedules (Non-Veg on Wed, Fri, Sun)
mixed_schedule_1 = {
    "Monday":    {"breakfast": "Poha with Peanuts", "lunch": "Chole with Rice", "snack": "Samosa", "dinner": "Paneer Butter Masala with Naan"},
    "Tuesday":   {"breakfast": "Idli with Coconut Chutney", "lunch": "Vegetable Biryani with Raita", "snack": "Murukku", "dinner": "Dal Tadka with Jeera Rice"},
    "Wednesday": {"breakfast": "Aloo Paratha with Yogurt", "lunch": "Chicken Curry with Rice", "snack": "Chicken Nuggets", "dinner": "Grilled Fish with Vegetables"},
    "Thursday":  {"breakfast": "Uttapam with Tomato Chutney", "lunch": "Pulao with Mixed Vegetables", "snack": "Chivda", "dinner": "Baingan Bharta with Roti"},
    "Friday":    {"breakfast": "Dosa with Sambar", "lunch": "Prawn Masala with Chapati", "snack": "Fish Cutlet", "dinner": "Butter Chicken with Naan"},
    "Saturday":  {"breakfast": "Wheat Flour Pancakes", "lunch": "Methi Thepla with Yogurt", "snack": "Pakora", "dinner": "Rajma Curry with Rice"},
    "Sunday":    {"breakfast": "French Toast (Indian style)", "lunch": "Mutton Biryani with Raita", "snack": "Chicken Tikka", "dinner": "Fish Curry with Rice"}
}

mixed_schedule_2 = {
    "Monday":    {"breakfast": "Moong Dal Chilla", "lunch": "Rajma with Jeera Rice", "snack": "Kachori", "dinner": "Aloo Gobi with Roti"},
    "Tuesday":   {"breakfast": "Upma with Coconut Chutney", "lunch": "Bhindi Masala with Roti", "snack": "Sev Puri", "dinner": "Dal Makhani with Naan"},
    "Wednesday": {"breakfast": "Egg Bhurji with Toast", "lunch": "Chicken Biryani with Raita", "snack": "Chicken Pakora", "dinner": "Tandoori Chicken with Roti"},
    "Thursday":  {"breakfast": "Besan Chilla", "lunch": "Pulao with Curd", "snack": "Dhokla", "dinner": "Paneer Kofta with Naan"},
    "Friday":    {"breakfast": "Omelette with Paratha", "lunch": "Fish Masala with Jeera Rice", "snack": "Prawn Cutlet", "dinner": "Mutton Kadai with Paratha"},
    "Saturday":  {"breakfast": "Sabudana Khichdi", "lunch": "Baingan Bharta with Roti", "snack": "Chivda", "dinner": "Khichdi with Kadhi"},
    "Sunday":    {"breakfast": "Egg Sandwich", "lunch": "Mutton Rogan Josh with Rice", "snack": "Chicken Momos", "dinner": "Fish Tikka with Lemon Rice"}
}

mixed_schedule_3 = {
    "Monday":    {"breakfast": "Vermicelli Upma", "lunch": "Dal Palak with Roti", "snack": "Bread Pakora", "dinner": "Matar Paneer with Naan"},
    "Tuesday":   {"breakfast": "Rava Dosa with Chutney", "lunch": "Capsicum Besan Sabji with Rice", "snack": "Aloo Tikki", "dinner": "Mixed Vegetable Curry with Chapati"},
    "Wednesday": {"breakfast": "Boiled Eggs with Salad", "lunch": "Chicken Korma with Rice", "snack": "Chicken Popcorn", "dinner": "Mutton Keema with Paratha"},
    "Thursday":  {"breakfast": "Oats Pancakes", "lunch": "Rajma with Rice", "snack": "Chana Chaat", "dinner": "Kadhi Pakora with Rice"},
    "Friday":    {"breakfast": "Scrambled Eggs with Roti", "lunch": "Prawn Pulao with Raita", "snack": "Fish Fingers", "dinner": "Butter Chicken with Naan"},
    "Sunday":    {"breakfast": "Chicken Poha", "lunch": "Fish Curry with Basmati Rice", "snack": "Chicken Seekh Kebab", "dinner": "Tandoori Chicken with Roti"}
}

insert_schedule("mixed", mixed_schedule_1)
insert_schedule("mixed", mixed_schedule_2)
insert_schedule("mixed", mixed_schedule_3)

conn.close()
print("✅ Mixed schedules inserted successfully!")
