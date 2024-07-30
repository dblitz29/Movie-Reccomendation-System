import pandas as pd
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import faiss
import pickle

# Load and preprocess data
data = pd.read_csv('/home/ubuntu/fadil/_Side/dataset/wiki_movie_plots_deduped.csv')
data_cleaned = data.dropna(subset=['Plot'])
data_cleaned['Plot'] = data_cleaned['Plot'].str.lower()

# Generate embeddings
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-MiniLM-L6-v2')
model = AutoModel.from_pretrained('sentence-transformers/all-MiniLM-L6-v2').cuda()

def generate_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512).to('cuda')
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings

plots = data_cleaned['Plot'].tolist()
embeddings = torch.cat([generate_embeddings(plot) for plot in plots], dim=0)
embeddings_np = embeddings.cpu().numpy()

# Encode additional features
one_hot_encoder = OneHotEncoder()
additional_features = data_cleaned[['Genre', 'Origin/Ethnicity']].fillna('')
encoded_features = one_hot_encoder.fit_transform(additional_features).toarray()

# Combine features
combined_features = np.hstack((embeddings_np, encoded_features))

# Build FAISS index
d = combined_features.shape[1]
index = faiss.IndexFlatL2(d)
index.add(combined_features)

# Save preprocessed data, embeddings, and FAISS index
data_cleaned.to_pickle('data_cleaned.pkl')
with open('embeddings_np.pkl', 'wb') as f:
    pickle.dump(embeddings_np, f)
with open('encoded_features.pkl', 'wb') as f:
    pickle.dump(encoded_features, f)
faiss.write_index(index, 'faiss_index.index')
with open('one_hot_encoder.pkl', 'wb') as f:
    pickle.dump(one_hot_encoder, f)
