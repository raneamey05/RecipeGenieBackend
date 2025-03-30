import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("recipes.db")
cursor = conn.cursor()

# Create the weekly_schedule table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS weekly_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    schedule_type TEXT NOT NULL,  -- veg, nonveg, mixed
    day TEXT NOT NULL,
    breakfast TEXT NOT NULL,
    lunch TEXT NOT NULL,
    snack TEXT NOT NULL,
    dinner TEXT NOT NULL
)
""")

# Function to insert weekly schedules
def insert_schedule(schedule_type, schedule_data):
    for day, meals in schedule_data.items():
        cursor.execute("""
        INSERT INTO weekly_schedule (schedule_type, day, breakfast, lunch, snack, dinner) 
        VALUES (?, ?, ?, ?, ?, ?)
        """, (schedule_type, day, meals["breakfast"], meals["lunch"], meals["snack"], meals["dinner"]))
    conn.commit()

# Proper Vegetarian Weekly Schedules
veg_schedule_1 = {
    "Monday":    {"breakfast": "Poha", "lunch": "Chole with Rice", "snack": "Samosa", "dinner": "Paneer Butter Masala with Naan"},
    "Tuesday":   {"breakfast": "Idli with Coconut Chutney", "lunch": "Vegetable Biryani with Raita", "snack": "Murukku", "dinner": "Dal Tadka with Jeera Rice"},
    "Wednesday": {"breakfast": "Aloo Paratha with Yogurt", "lunch": "Palak Paneer with Chapati", "snack": "Dhokla", "dinner": "Matar Paneer with Roti"},
    "Thursday":  {"breakfast": "Uttapam with Tomato Chutney", "lunch": "Pulao with Mixed Vegetables", "snack": "Chivda", "dinner": "Baingan Bharta with Roti"},
    "Friday":    {"breakfast": "Dosa with Sambar", "lunch": "Rajma with Rice", "snack": "Pani Puri", "dinner": "Stuffed Capsicum with Roti"},
    "Saturday":  {"breakfast": "Besan Chilla", "lunch": "Methi Thepla with Yogurt", "snack": "Pakora", "dinner": "Vegetable Pulao with Raita"},
    "Sunday":    {"breakfast": "French Toast", "lunch": "Kadai Paneer with Naan", "snack": "Kachori", "dinner": "Dal Makhani with Jeera Rice"}
}

veg_schedule_2 = {
    "Monday":    {"breakfast": "Masala Dosa", "lunch": "Dal Fry with Rice", "snack": "Sev Puri", "dinner": "Mix Vegetable Curry with Chapati"},
    "Tuesday":   {"breakfast": "Moong Dal Chilla", "lunch": "Chana Masala with Rice", "snack": "Pav Bhaji", "dinner": "Paneer Tikka with Green Chutney"},
    "Wednesday": {"breakfast": "Aloo Puri", "lunch": "Veg Fried Rice with Manchurian", "snack": "Masala Corn", "dinner": "Rajma Curry with Paratha"},
    "Thursday":  {"breakfast": "Methi Paratha", "lunch": "Bhindi Masala with Roti", "snack": "Dhokla", "dinner": "Stuffed Karela with Rice"},
    "Friday":    {"breakfast": "Rava Idli", "lunch": "Mushroom Masala with Rice", "snack": "Samosa", "dinner": "Aloo Gobi with Paratha"},
    "Saturday":  {"breakfast": "Vegetable Upma", "lunch": "Dum Aloo with Naan", "snack": "Chakli", "dinner": "Kadhi Pakora with Jeera Rice"},
    "Sunday":    {"breakfast": "Cornflakes with Milk", "lunch": "Vegetable Kofta with Roti", "snack": "Fruit Salad", "dinner": "Mix Veg Biryani with Raita"}
}

veg_schedule_3 = {
    "Monday":    {"breakfast": "Sprouts Salad", "lunch": "Methi Malai Matar with Chapati", "snack": "Khakhra", "dinner": "Baingan Bharta with Roti"},
    "Tuesday":   {"breakfast": "Bread Upma", "lunch": "Aloo Matar with Rice", "snack": "Pani Puri", "dinner": "Lauki Kofta with Chapati"},
    "Wednesday": {"breakfast": "Vegetable Sandwich", "lunch": "Dal Tadka with Rice", "snack": "Moong Dal Ladoo", "dinner": "Bhindi Fry with Roti"},
    "Thursday":  {"breakfast": "Idli with Sambar", "lunch": "Rajma Masala with Rice", "snack": "Mathri", "dinner": "Gobi Paratha with Yogurt"},
    "Friday":    {"breakfast": "Besan Chilla", "lunch": "Vegetable Korma with Roti", "snack": "Makhana Chaat", "dinner": "Palak Paneer with Jeera Rice"},
    "Saturday":  {"breakfast": "Aloo Poha", "lunch": "Dal Palak with Roti", "snack": "Veg Cutlet", "dinner": "Paneer Bhurji with Paratha"},
    "Sunday":    {"breakfast": "Sheera (Sooji Halwa)", "lunch": "Chole Bhature", "snack": "Banana Chips", "dinner": "Vegetable Handi with Tandoori Roti"}
}

# Insert all 3 proper vegetarian schedules into the database
insert_schedule("veg", veg_schedule_1)
insert_schedule("veg", veg_schedule_2)
insert_schedule("veg", veg_schedule_3)

# Close the database connection
conn.close()

print("✅ Weekly schedule table created and vegetarian schedules inserted successfully!")
