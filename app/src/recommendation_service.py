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

# Compute product popularity using Bayesian Average
m = 5  # Minimum number of ratings to be considered
C = interactions['rating'].mean()  # Overall average rating

product_popularity = interactions.groupby('product_id')['rating'].agg(['mean', 'count']).reset_index()
product_popularity.columns = ['product_id', 'avg_rating', 'num_ratings']

# Bayesian Average Popularity Score
product_popularity['popularity_score'] = (
    (product_popularity['avg_rating'] * product_popularity['num_ratings'] + C * m) /
    (product_popularity['num_ratings'] + m)
)

# Merge popularity into products dataframe
products = products.merge(product_popularity, on='product_id', how='left').fillna(0)

def get_product_by_id(product_id: int):
    return products[products["product_id"] == product_id].to_dict(orient="records")[0]

# Function to recommend products based on user interactions
def recommend_products(user_id, top_n=5):
    user_ratings = interactions[interactions['user_id'] == user_id]
    
    if user_ratings.empty:
        # Cold Start: Recommend trending products (high popularity & in stock)
        trending_products = products[products["stock"] > 0].nlargest(top_n, 'popularity_score')
        return list(zip(trending_products['product_id'], trending_products['popularity_score']))

    scored_products = {}

    # User's preferred categories and brands (weighted by rating)
    user_products = user_ratings.merge(products, on="product_id")
    preferred_categories = user_products.groupby("category")['rating'].mean().nlargest(2).index
    preferred_brands = user_products.groupby("brand")['rating'].mean().nlargest(2).index

    for _, row in user_ratings.iterrows():
        product_idx = products[products['product_id'] == row['product_id']].index[0]
        similarity_scores = cosine_sim[product_idx]

        for idx, score in enumerate(similarity_scores):
            product_id = products.iloc[idx]['product_id']
            if product_id in user_ratings['product_id'].values:
                continue  # Skip already rated products
            
            # Weighted Score Calculation
            weighted_score = (
                score * row['rating'] +  # Content Similarity × User Rating
                products.iloc[idx]['popularity_score'] * 0.2 +  # Boost Popularity Score
                (2.5 if products.iloc[idx]['category'] in preferred_categories else 0) +  # Category Weight
                (1.5 if products.iloc[idx]['brand'] in preferred_brands else 0) +  # Brand Weight
                (1 if products.iloc[idx]['stock'] > 0 else -0.5)  # Stock Availability
            )
            
            scored_products[product_id] = scored_products.get(product_id, 0) + weighted_score

    # Normalize Scores to a 0-1 range
    if scored_products:
        min_score = min(scored_products.values())
        max_score = max(scored_products.values())
        for k in scored_products:
            scored_products[k] = (scored_products[k] - min_score) / (max_score - min_score + 1e-9)

    # Sort products based on scores
    sorted_products = sorted(scored_products.items(), key=lambda x: x[1], reverse=True)
    
    # Return top N recommendations
    return sorted_products[:top_n]

# Categorize recommendations
def categorize_recommendations(user_id):
    recommendations = recommend_products(user_id)
    if not recommendations:
        return None  # No recommendations available
    
    categories = {"Highly Recommended": [], "Recommended": [], "Not Recommended": []}
    
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
