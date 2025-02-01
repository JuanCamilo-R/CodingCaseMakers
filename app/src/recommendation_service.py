from app.src.data import products, interactions
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Vectorization using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(products['description'])

# Compute cosine similarity between products
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend products based on user interactions
def recommend_products(user_id):
    user_ratings = interactions[interactions['user_id'] == user_id]
    
    if user_ratings.empty:
        return None  # No recommendations if the user has no interactions
    
    scored_products = {}
    
    for _, row in user_ratings.iterrows():
        product_idx = products[products['product_id'] == row['product_id']].index[0]
        similarity_scores = cosine_sim[product_idx]
        
        for idx, score in enumerate(similarity_scores):
            if idx not in scored_products:
                scored_products[idx] = 0
            scored_products[idx] += score * row['rating']  # Weight by rating
    
    # Sort products based on scores
    sorted_products = sorted(scored_products.items(), key=lambda x: x[1], reverse=True)
    
    recommendations = []
    for idx, score in sorted_products:
        product_id = products.iloc[idx]['product_id']
        if product_id not in user_ratings['product_id'].values:
            recommendations.append((product_id, score))
    
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
            if score >= threshold_high:
                categories["Highly Recommended"].append(product_id)
            elif score >= threshold_low:
                categories["Recommended"].append(product_id)
            else:
                categories["Not Recommended"].append(product_id)
    
    return categories

# Generate recommendations for a sample user
user_id = 1
recommendations = categorize_recommendations(user_id)
print(recommendations)
