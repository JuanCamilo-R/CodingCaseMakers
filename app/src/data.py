import pandas as pd

# Creating the corrected products DataFrame
import pandas as pd

# Define product data with reasonable price estimates
products = pd.DataFrame([
    {"product_id": 1, "name": "HP Laptop", "category": "Laptop", "brand": "HP",
     "description": "15.6-inch FHD display, Intel i7, 16GB RAM, 512GB SSD.", "price": 999.99, "stock": 50},
    {"product_id": 2, "name": "Dell Laptop", "category": "Laptop", "brand": "Dell",
     "description": "14-inch HD display, Intel i5, 8GB RAM, 256GB SSD.", "price": 749.99, "stock": 40},
    {"product_id": 3, "name": "Apple MacBook", "category": "Laptop", "brand": "Apple",
     "description": "13-inch Retina display, M1 chip, 16GB RAM, 512GB SSD.", "price": 1299.99, "stock": 30},
    {"product_id": 4, "name": "HP Monitor", "category": "Monitor", "brand": "HP",
     "description": "24-inch LED, 1080p Full HD, 60Hz refresh rate.", "price": 199.99, "stock": 60},
    {"product_id": 5, "name": "Dell Ultrasharp Monitor", "category": "Monitor", "brand": "Dell",
     "description": "27-inch 4K UHD, IPS display, HDR support.", "price": 499.99, "stock": 35},
    {"product_id": 6, "name": "Apple iPad Pro", "category": "Tablet", "brand": "Apple",
     "description": "12.9-inch Liquid Retina, M2 chip, 256GB storage.", "price": 1099.99, "stock": 25},
    {"product_id": 7, "name": "Samsung Galaxy Tab", "category": "Tablet", "brand": "Samsung",
     "description": "11-inch LCD display, 6GB RAM, 128GB storage.", "price": 599.99, "stock": 45},
    {"product_id": 8, "name": "Lenovo ThinkPad", "category": "Laptop", "brand": "Lenovo",
     "description": "14-inch FHD, Intel i7, 16GB RAM, 1TB SSD.", "price": 1149.99, "stock": 20},
    {"product_id": 9, "name": "Asus ROG Gaming Laptop", "category": "Laptop", "brand": "Asus",
     "description": "17-inch QHD, Ryzen 9, RTX 4070, 32GB RAM, 1TB SSD.", "price": 1999.99, "stock": 15},
    {"product_id": 10, "name": "Microsoft Surface Pro", "category": "Tablet", "brand": "Microsoft",
     "description": "13-inch touchscreen, Intel i5, 8GB RAM, 256GB SSD.", "price": 899.99, "stock": 30},
    {"product_id": 11, "name": "Razer Blade Gaming Laptop", "category": "Laptop", "brand": "Razer",
     "description": "15-inch OLED, Intel i9, RTX 4080, 32GB RAM, 1TB SSD.", "price": 2499.99, "stock": 10},
    {"product_id": 12, "name": "LG UltraFine Monitor", "category": "Monitor", "brand": "LG",
     "description": "32-inch 4K UHD, HDR 600, 144Hz refresh rate.", "price": 699.99, "stock": 25},
    {"product_id": 13, "name": "Sony Bravia OLED TV", "category": "TV", "brand": "Sony",
     "description": "55-inch 4K HDR OLED, Dolby Vision, Smart TV.", "price": 1499.99, "stock": 12},
    {"product_id": 14, "name": "Samsung QLED TV", "category": "TV", "brand": "Samsung",
     "description": "65-inch QLED, 4K HDR, 120Hz refresh rate, Smart TV.", "price": 1799.99, "stock": 18},
    {"product_id": 15, "name": "Bose Noise Cancelling Headphones", "category": "Audio", "brand": "Bose",
     "description": "Wireless, 30-hour battery life, Active Noise Cancelling.", "price": 349.99, "stock": 55},
    {"product_id": 16, "name": "Sony WH-1000XM5", "category": "Audio", "brand": "Sony",
     "description": "Over-ear headphones, ANC, Hi-Res Audio, 40-hour battery.", "price": 399.99, "stock": 50},
    {"product_id": 17, "name": "Apple AirPods Pro", "category": "Audio", "brand": "Apple",
     "description": "Wireless earbuds, Spatial Audio, Active Noise Cancelling.", "price": 249.99, "stock": 65},
    {"product_id": 18, "name": "JBL Bluetooth Speaker", "category": "Audio", "brand": "JBL",
     "description": "Portable, waterproof, 20-hour battery, deep bass sound.", "price": 129.99, "stock": 70},
    {"product_id": 19, "name": "Google Pixel Tablet", "category": "Tablet", "brand": "Google",
     "description": "11-inch LCD, Tensor G2, 128GB storage, Android 13.", "price": 699.99, "stock": 22},
])

# Correcting interactions DataFrame (removing syntax errors and ensuring consistency)
interactions = pd.DataFrame([
    # User 1 Interactions
    {"user_id": 1, "product_id": 1, "rating": 5.0},
    {"user_id": 1, "product_id": 2, "rating": 4.0},
    {"user_id": 1, "product_id": 8, "rating": 3.9},
    {"user_id": 1, "product_id": 9, "rating": 4.8},
    {"user_id": 1, "product_id": 10, "rating": 3.5},
    {"user_id": 1, "product_id": 15, "rating": 4.4},
    {"user_id": 1, "product_id": 16, "rating": 3.8},
    
    # User 2 Interactions
    {"user_id": 2, "product_id": 1, "rating": 3.0},
    {"user_id": 2, "product_id": 2, "rating": 4.2},
    {"user_id": 2, "product_id": 3, "rating": 4.0},
    {"user_id": 2, "product_id": 4, "rating": 4.5},
    {"user_id": 2, "product_id": 5, "rating": 3.8},
    {"user_id": 2, "product_id": 10, "rating": 4.6},
    {"user_id": 2, "product_id": 11, "rating": 3.7},
    {"user_id": 2, "product_id": 12, "rating": 4.1},
    {"user_id": 2, "product_id": 13, "rating": 3.6},

    # User 3 Interactions
    {"user_id": 3, "product_id": 6, "rating": 4.1},
    {"user_id": 3, "product_id": 7, "rating": 4.5},
    {"user_id": 3, "product_id": 8, "rating": 3.9},
    {"user_id": 3, "product_id": 9, "rating": 4.8},
    {"user_id": 3, "product_id": 10, "rating": 3.5},
    {"user_id": 3, "product_id": 11, "rating": 4.6},
    {"user_id": 3, "product_id": 12, "rating": 3.7},
    {"user_id": 3, "product_id": 13, "rating": 4.0},
    {"user_id": 3, "product_id": 14, "rating": 3.6},
])
