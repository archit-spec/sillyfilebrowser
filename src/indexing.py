import faiss
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from captioning import ImageCaptioning

# Load pre-trained text embedding model (e.g., Sentence Transformer)
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# Function to embed text queries (customize based on your model)
def embed_text(text_query):
    encoded_input = tokenizer(text_query, return_tensors="pt")
    with torch.no_grad():
        features = model(**encoded_input)
    return features[0].mean(dim=0).cpu().numpy()  # Average pooled hidden state

# Load pre-trained image feature extractor (e.g., EfficientNet)
from transformers import CLIPProcessor, CLIPModel
feature_extractor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

# Function to extract image features (customize based on your model)
def extract_image_features(image_path):
    image = feature_extractor(image_path, return_tensors="pt")
    with torch.no_grad():
        features = model.encode_image(**image)
    return features[0].cpu().numpy()  # Image features

# Load your dataset of images and their corresponding textual descriptions
def load_dataset(a, b):
    image_paths = a # List of image paths
    descriptions = b  # List of textual descriptions for each image
    return image_paths, descriptions

# Create FAISS index for efficient similarity search
def create_faiss_index(image_features):
    d = image_features.shape[1]  # Dimensionality of image features
    index = faiss.IndexFlatL2(d)
    index.add(np.ascontiguousarray(image_features))
    return index

# Text-to-image search function
def search_images(text_query, index, image_features, top_k=5):
    text_embedding = embed_text(text_query)
    distances, indices = index.search(text_embedding.reshape(1, -1), top_k)
    return [image_paths[i] for i in indices.ravel()]

# Example usage
alo = ImageCaptioning()
dic = alo.make_index()

a = list(dic.keys())
b = list(dic.values())

image_paths, descriptions = load_dataset(a,b)
image_features = [extract_image_features(path) for path in image_paths]
index = create_faiss_index(image_features)

text_query = "A cat sitting on a chair"
results = search_images(text_query, index, image_paths)
print(f"Top {len(results)} similar images for '{text_query}':")
for image_path in results:
    print(image_path)

