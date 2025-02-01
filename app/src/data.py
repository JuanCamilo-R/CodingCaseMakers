import pandas as pd

products = pd.DataFrame([
    {"product_id": 1, "name": "HP Laptop", "category": "Laptop", "brand": "HP",
     "description": "15.6-inch FHD display, Intel i7, 16GB RAM, 512GB SSD."},
    {"product_id": 2, "name": "Dell Laptop", "category": "Laptop", "brand": "Dell",
     "description": "14-inch HD display, Intel i5, 8GB RAM, 256GB SSD."},
    {"product_id": 3, "name": "Apple MacBook", "category": "Laptop", "brand": "Apple",
     "description": "13-inch Retina display, M1 chip, 16GB RAM, 512GB SSD."},
    {"product_id": 4, "name": "HP Monitor", "category": "Monitor", "brand": "HP",
     "description": "24-inch LED, 1080p Full HD, 60Hz refresh rate."},
    {"product_id": 5, "name": "Dell Ultrasharp Monitor", "category": "Monitor", "brand": "Dell",
     "description": "27-inch 4K UHD, IPS display, HDR support."},
    {"product_id": 6, "name": "Apple iPad Pro", "category": "Tablet", "brand": "Apple",
     "description": "12.9-inch Liquid Retina, M2 chip, 256GB storage."},
    {"product_id": 7, "name": "Samsung Galaxy Tab", "category": "Tablet", "brand": "Samsung",
     "description": "11-inch LCD display, 6GB RAM, 128GB storage."},
    {"product_id": 8, "name": "Lenovo ThinkPad", "category": "Laptop", "brand": "Lenovo",
     "description": "14-inch FHD, Intel i7, 16GB RAM, 1TB SSD."},
    {"product_id": 9, "name": "Asus ROG Gaming Laptop", "category": "Laptop", "brand": "Asus",
     "description": "17-inch QHD, Ryzen 9, RTX 4070, 32GB RAM, 1TB SSD."},
    {"product_id": 10, "name": "Microsoft Surface Pro", "category": "Tablet", "brand": "Microsoft",
     "description": "13-inch touchscreen, Intel i5, 8GB RAM, 256GB SSD."},
    {"product_id": 11, "name": "Razer Blade Gaming Laptop", "category": "Laptop", "brand": "Razer",
     "description": "15-inch OLED, Intel i9, RTX 4080, 32GB RAM, 1TB SSD."},
    {"product_id": 12, "name": "LG UltraFine Monitor", "category": "Monitor", "brand": "LG",
     "description": "32-inch 4K UHD, HDR 600, 144Hz refresh rate."},
    {"product_id": 13, "name": "Sony Bravia OLED TV", "category": "TV", "brand": "Sony",
     "description": "55-inch 4K HDR OLED, Dolby Vision, Smart TV."},
    {"product_id": 14, "name": "Samsung QLED TV", "category": "TV", "brand": "Samsung",
     "description": "65-inch QLED, 4K HDR, 120Hz refresh rate, Smart TV."},
    {"product_id": 15, "name": "Bose Noise Cancelling Headphones", "category": "Audio", "brand": "Bose",
     "description": "Wireless, 30-hour battery life, Active Noise Cancelling."},
    {"product_id": 16, "name": "Sony WH-1000XM5", "category": "Audio", "brand": "Sony",
     "description": "Over-ear headphones, ANC, Hi-Res Audio, 40-hour battery."},
    {"product_id": 17, "name": "Apple AirPods Pro", "category": "Audio", "brand": "Apple",
     "description": "Wireless earbuds, Spatial Audio, Active Noise Cancelling."},
    {"product_id": 18, "name": "JBL Bluetooth Speaker", "category": "Audio", "brand": "JBL",
     "description": "Portable, waterproof, 20-hour battery, deep bass sound."},
    {"product_id": 19, "name": "Google Pixel Tablet", "category": "Tablet", "brand": "Google",
     "description": "11-inch LCD, Tensor G2, 128GB storage, Android 13."},
])

interactions = pd.DataFrame([
    # User 1 Interactions
    {"user_id": 1, "product_id": 1, "interaction_type": "purchased", "rating": 5.0},
    {"user_id": 1, "product_id": 2, "interaction_type": "viewed", "rating": 4.0},
    {"user_id": 1, "product_id": 9, "interaction_type": "purchased", "rating": 4.8},
    {"user_id": 1, "product_id": 14, "interaction_type": "viewed", "rating": 3.5},
    
    # User 2 Interactions
    {"user_id": 2, "product_id": 2, "interaction_type": "purchased", "rating": 3.0},
    {"user_id": 2, "product_id": 3, "interaction_type": "viewed", "rating": 4.0},
    {"user_id": 2, "product_id": 7, "interaction_type": "viewed", "rating": 4.5},
    {"user_id": 2, "product_id": 16, "interaction_type": "purchased", "rating": 4.7},

    # User 3 Interactions
    {"user_id": 3, "product_id": 1, "interaction_type": "viewed", "rating": 2.5},
    {"user_id": 3, "product_id": 4, "interaction_type": "purchased", "rating": 4.2},
    {"user_id": 3, "product_id": 5, "interaction_type": "viewed", "rating": 3.8},
    {"user_id": 3, "product_id": 17, "interaction_type": "purchased", "rating": 4.9},
])