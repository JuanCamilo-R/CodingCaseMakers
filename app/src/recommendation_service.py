from app.src.data import products, interactions
import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Vectorization using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(products['description'])

# Compute cosine similarity between products
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Compute product popularity based on average rating
product_popularity = interactions.groupby('product_id')['rating'].agg(['mean', 'count']).reset_index()
product_popularity.columns = ['product_id', 'avg_rating', 'num_ratings']

# Normalize popularity score
product_popularity['popularity_score'] = (
    product_popularity['avg_rating'] * product_popularity['num_ratings']
) / product_popularity['num_ratings'].max()

# Merge popularity into products dataframe
products = products.merge(product_popularity, on='product_id', how='left').fillna(0)

def get_product_by_id(product_id: int):
    return products[products["product_id"] == product_id].to_dict(orient="records")[0]

# Function to recommend products based on user interactions
def recommend_products(user_id, top_n=5):
    user_ratings = interactions[interactions['user_id'] == user_id]
    
    if user_ratings.empty:
        return []  # Return an empty list if the user has no interactions
    
    scored_products = {}

    # User's preferred categories and brands
    preferred_categories = user_ratings.merge(products, on="product_id")["category"].value_counts().index[:2]
    preferred_brands = user_ratings.merge(products, on="product_id")["brand"].value_counts().index[:2]

    for _, row in user_ratings.iterrows():
        product_idx = products[products['product_id'] == row['product_id']].index[0]
        similarity_scores = cosine_sim[product_idx]
        
        for idx, score in enumerate(similarity_scores):
            product_id = products.iloc[idx]['product_id']
            if product_id in user_ratings['product_id'].values:
                continue  # Skip already rated products
            
            # Weight by rating, popularity, and similarity
            weighted_score = (
                score * row['rating'] +  # Content Similarity × User Rating
                products.iloc[idx]['popularity_score'] * 0.1 +  
                (1 if products.iloc[idx]['category'] in preferred_categories else 0) * 2.0 +  # Category Weight
                (1 if products.iloc[idx]['brand'] in preferred_brands else 0) * 1.0 +  # Brand Weight
                (1 if products.iloc[idx]['stock'] > 0 else -0.5)  # Stock Availability
            )
            
            if product_id not in scored_products:
                scored_products[product_id] = 0
            scored_products[product_id] += weighted_score

    # Sort products based on scores
    sorted_products = sorted(scored_products.items(), key=lambda x: x[1], reverse=True)
    
    # Return top N recommendations as (product_id, score) tuples
    recommendations = [(product_id, score) for product_id, score in sorted_products[:top_n]]
    
    return recommendations
# Categorize recommendations
def categorize_recommendations(user_id):
    recommendations = recommend_products(user_id)
    if not recommendations:
        return None  # No recommendations available
    
    categories = {"Highly Recommended": [], "Recommended": [], "Not Recommended": []}
    
    if recommendations:
        scores = [score for _, score in recommendations]
        threshold_high = np.percentile(scores, 75)
        threshold_low = np.percentile(scores, 25)
        
        for product_id, score in recommendations:
            product = get_product_by_id(product_id)
            if score >= threshold_high:
                categories["Highly Recommended"].append(product)
            elif score >= threshold_low:
                categories["Recommended"].append(product)
            else:
                categories["Not Recommended"].append(product)
    
    return categories
