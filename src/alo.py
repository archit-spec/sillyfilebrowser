import faiss
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModel
from captioning import ImageCaptioning
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import joblib
from concurrent.futures import ThreadPoolExecutor


# Load pre-trained text embedding model (e.g., Sentence Transformer)
text_tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
text_model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")
feature_extractor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
image_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

# Function to embed text queries (customize based on your model)
#@joblib.cache
def embed_text(text_query):
    encoded_input = text_tokenizer(text_query, return_tensors="pt")
    with torch.no_grad():
        output = text_model(**encoded_input)
    return output.last_hidden_state.mean(dim=1).cpu().numpy()

# Function to extract image features (customize based on your model)
#@joblib.cache
def extract_image_features(image_path):
    image = Image.open(image_path)
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        output = image_model.get_image_features(**inputs)
    return output.cpu().numpy()

# Load your dataset of images and their corresponding textual descriptions
def load_dataset(image_paths, descriptions):
    return image_paths, descriptions

# Create FAISS index for efficient similarity search
#def create_faiss_index(image_features):
#    d = image_features.shape[1]  # Dimensionality of image features
#    index = faiss.IndexFlatL2(d)
#    index.add(np.ascontiguousarray(image_features))
#    return index
def create_faiss_index(image_features):
    image_features = np.concatenate(image_features, axis=0)  # Concatenate the individual NumPy arrays
    d = image_features.shape[1]  # Dimensionality of image features
    index = faiss.IndexFlatL2(d)
    index.add(np.ascontiguousarray(image_features))
    return index

# Text-to-image search function
def search_images(text_query, index, image_paths, top_k=5):
    text_embedding = embed_text(text_query)
    distances, indices = index.search(text_embedding.reshape(1, -1), top_k)
    return [image_paths[i] for i in indices.ravel()]

# Example usage
alo = ImageCaptioning()
my_dict = alo.make_index()
image_paths = list(my_dict.keys())
descriptions = [item for sublist in list(my_dict.values()) for item in sublist]

print("Image paths:", image_paths, "\n", "Descriptions:", descriptions)

image_features = [extract_image_features(path) for path in image_paths]
index = create_faiss_index(image_features)

text_query = input("Enter your query: ")
results = search_images(text_query, index, image_paths)

print(f"Top {len(results)} similar images for '{text_query}':")
for image_path in results:
    print(image_path)
