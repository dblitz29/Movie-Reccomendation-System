#!/usr/bin/env python3

import pandas as pd
import faiss
import pickle
import numpy as np
import argparse
import os
import json

# Define the directory where the files are saved
save_dir = os.path.join(os.path.dirname(__file__), '/home/ubuntu/fadil/_Side/1.3_(JS)Movie Reccomendation')

# Load preprocessed data and FAISS index
data_cleaned = pd.read_pickle(os.path.join(save_dir, 'data_cleaned.pkl'))
with open(os.path.join(save_dir, 'embeddings_np.pkl'), 'rb') as f:
    embeddings_np = pickle.load(f)
with open(os.path.join(save_dir, 'encoded_features.pkl'), 'rb') as f:
    encoded_features = pickle.load(f)
index = faiss.read_index(os.path.join(save_dir, 'faiss_index.index'))
with open(os.path.join(save_dir, 'one_hot_encoder.pkl'), 'rb') as f:
    one_hot_encoder = pickle.load(f)

# Combine features
combined_features = np.hstack((embeddings_np, encoded_features))

def recommend_movies_faiss(title, n_recommendations=10, genre=None, origin=None):
    if title not in data_cleaned['Title'].values:
        return [f"Title '{title}' not found in the dataset."]
    
    idx = data_cleaned[data_cleaned['Title'] == title].index[0]
    query_embedding = combined_features[idx].reshape(1, -1)
    distances, indices = index.search(query_embedding, n_recommendations + 1)
    movie_indices = indices.flatten()[1:]
    
    recommendations = data_cleaned.iloc[movie_indices]
    
    if genre:
        recommendations = recommendations[recommendations['Genre'].str.contains(genre, case=False, na=False)]
    if origin:
        recommendations = recommendations[recommendations['Origin/Ethnicity'].str.contains(origin, case=False, na=False)]
    
    return recommendations['Title'].tolist()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Movie Recommendation System')
    parser.add_argument('title', type=str, help='Movie title for recommendation')
    parser.add_argument('--genre', type=str, help='Genre filter for recommendation', default=None)
    parser.add_argument('--origin', type=str, help='Origin filter for recommendation', default=None)
    parser.add_argument('--n_recommendations', type=int, help='Number of recommendations', default=10)
    args = parser.parse_args()
    
    recommendations = recommend_movies_faiss(args.title, args.n_recommendations, args.genre, args.origin)
    print(json.dumps(recommendations))  # Print JSON-formatted output