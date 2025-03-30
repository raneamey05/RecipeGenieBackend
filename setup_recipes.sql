CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE, -- Ensures no duplicate recipe names
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);

-- Insert recipes, preventing duplicates
INSERT OR IGNORE INTO recipes (name, ingredients, instructions) VALUES
    ('Pancakes', 'flour, sugar, butter, eggs, milk', 'Mix ingredients, cook on a pan until golden brown.'),
    ('Chocolate Cake', 'flour, sugar, butter, eggs, cocoa powder', 'Mix ingredients, bake at 350°F (175°C) for 30 minutes.'),
    ('Puran Poli', 'chana dal, jaggery, cardamom powder, wheat flour, ghee', 'Cook chana dal and jaggery, make dough with wheat flour, stuff with filling, and cook.'),
    ('Omelette', 'eggs, salt, pepper, oil', 'Beat eggs, season, cook in a pan with oil until firm.'),
    ('Vegetable Soup', 'carrot, onion, tomato, garlic, salt, water', 'Boil vegetables, blend, season with salt.'),
    ('Garlic Bread', 'bread, butter, garlic, parsley', 'Spread garlic butter on bread, bake until golden.'),
    ('Fruit Salad', 'banana, apple, orange, grapes, honey', 'Chop fruits, mix, drizzle with honey.'),
    ('Mango Shake', 'mango, milk, sugar', 'Blend mango, milk, and sugar until smooth.'),
    
    ('Butter Chicken', 'chicken, butter, cream, tomatoes, garlic, ginger, garam masala, cilantro', 
 '1) Marinate chicken pieces in yogurt, garlic, ginger, and garam masala for at least 1 hour. 
  2) In a pan, melt butter and sauté garlic and ginger until fragrant. 
  3) Add marinated chicken and cook until browned. 
  4) Stir in chopped tomatoes and simmer for 15 minutes. 
  5) Add cream and cook for another 5 minutes. 
  6) Garnish with cilantro and serve with naan or rice.'),
  
('Chickpea Curry', 'chickpeas, onions, tomatoes, garlic, ginger, cumin, coriander, coconut milk', 
 '1) Sauté chopped onions, garlic, and ginger in a pan until golden. 
  2) Add cumin and coriander, and cook for another minute. 
  3) Stir in chopped tomatoes and cook until soft. 
  4) Add cooked chickpeas and coconut milk, and simmer for 10-15 minutes. 
  5) Season with salt and serve with rice or bread.'),

('Palak Paneer', 'spinach, paneer, garlic, ginger, onions, cream, spices', 
 '1) Blanch spinach in boiling water, then blend into a smooth puree. 
  2) In a pan, sauté chopped onions, garlic, and ginger until golden. 
  3) Add the spinach puree and cook for a few minutes. 
  4) Add cubed paneer and cream, and simmer for 5-7 minutes. 
  5) Season with salt and serve with roti or naan.'),

('Samosas', 'potatoes, peas, spices, flour, oil', 
 '1) Boil and mash potatoes, then mix with cooked peas and spices. 
  2) Make a dough with flour and water, and let it rest. 
  3) Roll out the dough and cut into circles. 
  4) Fill each circle with the potato mixture and fold into a triangle. 
  5) Deep-fry until golden brown and serve with chutney.'),

('Biryani', 'basmati rice, chicken/lamb, yogurt, onions, spices, saffron', 
 '1) Marinate meat in yogurt and spices for at least 1 hour. 
  2) Cook basmati rice until 70% done and set aside. 
  3) In a pot, sauté onions until golden, then add marinated meat and cook until done. 
  4) Layer the partially cooked rice over the meat and sprinkle saffron on top. 
  5) Cover and cook on low heat for 20-25 minutes. Serve with raita.'),

('Dal Makhani', 'black lentils, kidney beans, butter, cream, tomatoes, spices', 
 '1) Soak lentils and kidney beans overnight, then cook until soft. 
  2) In a pan, melt butter and sauté onions, garlic, and ginger. 
  3) Add chopped tomatoes and spices, and cook until the oil separates. 
  4) Stir in the cooked lentils and beans, and simmer for 20 minutes. 
  5) Add cream and cook for another 5 minutes. Serve with rice or naan.'),

('Aloo Gobi', 'potatoes, cauliflower, turmeric, cumin, coriander, onions', 
 '1) Heat oil in a pan and sauté chopped onions until golden. 
  2) Add cumin seeds and let them splutter. 
  3) Add diced potatoes and cauliflower florets, along with turmeric and coriander. 
  4) Cover and cook until vegetables are tender, stirring occasionally. 
  5) Season with salt and serve with roti.'),

('Tandoori Chicken', 'chicken, yogurt, tandoori masala, lemon juice, garlic', 
 '1) Marinate chicken in yogurt, tandoori masala, lemon juice, and garlic for at least 2 hours. 
  2) Preheat the oven to 400°F (200°C). 
  3) Place marinated chicken on a baking tray and bake for 30-35 minutes, turning halfway. 
  4) Serve hot with naan and salad.'),

('Gulab Jamun', 'milk powder, flour, sugar, ghee, cardamom, rose water', 
 '1) Mix milk powder, flour, and a pinch of baking soda to form a dough. 
  2) Shape the dough into small balls and set aside. 
  3) Heat ghee in a pan and fry the balls until golden brown. 
  4) In another pot, prepare sugar syrup with water, sugar, and cardamom. 
  5) Soak the fried balls in the warm syrup for at least 30 minutes before serving.'),

('Chicken Curry', 'chicken, onions, tomatoes, garlic, ginger, spices, cilantro', 
 '1) Heat oil in a pot and sauté chopped onions until golden brown. 
  2) Add minced garlic and ginger, cooking for another minute. 
  3) Stir in chopped tomatoes and cook until soft. 
  4) Add chicken pieces and spices, cooking until the chicken is browned. 
  5) Pour in water and simmer until the chicken is cooked through. 
  6) Garnish with cilantro and serve with rice or bread.'),

('Chole Bhature', 'chickpeas, flour, yogurt, onions, tomatoes, spices', 
 '1) Soak chickpeas overnight and cook until tender. 
  2) In a pan, sauté onions and tomatoes with spices until thick. 
  3) Add cooked chickpeas and simmer for 10 minutes. 
  4) For bhature, mix flour, yogurt, and water to form a dough. 
  5) Roll out and deep-fry until puffed and golden. 
  6) Serve chickpeas with bhature.'),

('Paneer Tikka', 'paneer, yogurt, bell peppers, onions, spices', 
 '1) Marinate paneer cubes and vegetables in yogurt and spices for 1 hour. 
  2) Skewer the marinated paneer and vegetables. 
  3) Grill or bake until charred and cooked through. 
  4) Serve hot with mint chutney.'),

('Dhokla', 'gram flour, yogurt, turmeric, mustard seeds, green chilies', 
 '1) Mix gram flour, yogurt, turmeric, and water to form a batter. 
  2) Add baking soda and let it rest for 30 minutes. 
  3) Pour the batter into a greased steaming tray and steam for 15-20 minutes. 
  4) Temper mustard seeds and green chilies in oil, then pour over the steamed dhokla. 
  5) Cut into pieces and serve with green chutney.'),

('Pav Bhaji', 'mixed vegetables, pav bread, butter, spices, onions, cilantro', 
 '1) Boil and mash mixed vegetables with spices. 
  2) In a pan, heat butter and sauté onions until golden. 
  3) Add the mashed vegetable mixture and cook for a few minutes. 
  4) Toast pav bread in butter until golden. 
  5) Serve bhaji with buttered pav and chopped cilantro.');


CREATE TABLE IF NOT EXISTS harmful_combinations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient1 TEXT NOT NULL,
    ingredient2 TEXT NOT NULL,
    message TEXT
);

INSERT INTO harmful_combinations (ingredient1, ingredient2, message) VALUES
('milk', 'chicken', 'Avoid combining milk and chicken as it can cause indigestion.'),
('fish', 'milk', 'Avoid combining fish and milk as it might lead to skin issues.'),
('banana', 'milk', 'Avoid combining banana and milk as it may cause mucus buildup.'),
('milk', 'citrus', 'Avoid mixing milk with citrus as it may cause curdling and digestion issues.'),
('Alcohol', 'caffeine', 'Combining alcohol and caffeine can be dangerous as it masks intoxication effects.'),
('Garlic', 'Mint', 'Garlic and mint counteract each others effects, reducing their benefits.'),
('Cucumber', 'Tomato', 'Cucumber and tomato have different digestion times, which may cause bloating.'),
('Melon', 'Water', 'Melon and water together can slow digestion and cause stomach discomfort.'),
('Fruit', 'Yoghurt', 'Mixing fruit  and yogurt may cause fermentation and digestive issues.'),
('Cheese', 'Meat', 'Cheese and meat together can be heavy on digestion and increase acidity.'),
('Tomatoes', 'Pasta', 'Tomatoes in pasta can interfere with carbohydrate digestion due to acidity.'),
('Beans', 'Cheese', 'Beans and cheese together can lead to bloating and gas.'),
('Wine', 'Sweet Desserts', 'Sweet desserts can alter wine’s taste and make it acidic.'),
('Caffeine', 'Dairy', 'Caffeine reduces calcium absorption from dairy products.'),
('Salt', 'Sugar', 'Salt and sugar together may spike blood sugar levels unexpectedly.'),
('Eggs', 'Bacon', 'Eggs and bacon together can cause cholesterol overload.'),
('Potatoes', 'Meat', 'Potatoes and meat together slow digestion and cause bloating.'),
('Cabbage', 'Carrot', 'Cabbage and carrots contain opposing minerals, making them hard to digest together.'),
('Honey', 'Hot Water', 'Honey in hot water destroys its beneficial enzymes.'),
('Spinach', 'Dairy', 'Calcium in dairy can interfere with iron absorption from spinach.'),
('Fish', 'Dairy', 'Fish and dairy together may cause allergies and indigestion.'),
('Bananas', 'Yogurt', 'Bananas with yogurt can lead to mucus formation and digestion issues.'),
('Cheese', 'Fish', 'Cheese and fish together can cause digestive issues.'),
('Peanut Butter', 'Jelly', 'Peanut butter and jelly together create a sugar spike and imbalance nutrients.'),
('Sugar', 'Starch', 'Sugar and starch together slow digestion and cause fermentation.'),
('Fried Foods', 'Sugary Drinks', 'This combination increases fat storage and causes energy crashes.'),
('Caffeine', 'Alcohol', 'Caffeine masks alcohol’s effects, leading to higher consumption.'),
('Soya Sauce', 'Vinegar', 'Soy sauce and vinegar together may cause acidity issues.'),
('Fruit Juices', 'Dairy', 'Fruit juice and dairy together can lead to fermentation and bloating.'),
('Potatoes', 'Bananas', 'Potatoes and bananas together can slow digestion.'),
('Honey', 'Garlic', 'Honey and garlic mixed in large amounts can lead to low blood pressure.'),
('Cabbage', 'Beans', 'Cabbage and beans together can cause excessive gas and bloating.'),
('Spinach', 'Cheese', 'Cheese can block iron absorption from spinach.'),
('Pineapple', 'Dairy', 'Pineapple and dairy may cause curdling and digestive discomfort.'),
('Fried Foods', 'Starches', 'Fried foods and starches slow digestion and cause weight gain.'),
('Chili Peppers', 'Dairy', 'Dairy can neutralize chili’s capsaicin, reducing its effectiveness.'),
('Coconut', 'Citrus', 'Coconut and citrus together can cause acidity and bloating.'),
('Fruit', 'Meat', 'Meat and fruit together slow digestion due to different digestion times.'),
('Berries', 'Cream', 'Berries and cream together may cause acidity.'),
('Bananas', 'Icecream', 'Bananas and ice cream can lead to mucus buildup.'),
('Cabbage', 'Apples', 'Cabbage and apples together can cause bloating.'),
('Honey', 'Vinegar', 'Honey and vinegar together can lead to blood sugar imbalances.'),
('Caffeine', 'Chocolate', 'Too much caffeine and chocolate together can cause jitters.'),
('Spinach', 'Beets', 'Both contain oxalates, which can increase kidney stone risk.'),
('Potatoes', 'Corn', 'Potatoes and corn together can slow digestion.'),
('Coconut', 'Pineapple', 'Coconut and pineapple together may cause acidity.'),
('Garlic', 'Fish', 'Garlic and fish together can cause digestive irritation.');


