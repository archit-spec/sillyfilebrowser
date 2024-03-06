import streamlit as st
import os
from PIL import Image
from src.captioning import ImageCaptioning

def main():
    """Main function of the Streamlit application."""
    st.title("Image Explorer")

    # Get directory path from user input or set default
    default_dir = os.getcwd()  # Use current working directory as default
    user_dir = st.text_input("Enter directory path:", default_dir)
    if user_dir:
        dir_path = user_dir
    else:
        dir_path = default_dir

    # Check if directory exists
    if not os.path.exists(dir_path):
        st.error(f"Directory '{dir_path}' does not exist")
        return

    # Create an instance of ImageCaptioning and generate the index
    image_captioning = ImageCaptioning()
    image_dict = image_captioning.make_index(dir_path)

    # Add search bar
    search_term = st.text_input("Search images by description:", "")

    # Filter images based on search term
    filtered_images = [
        (image_path, descriptions)
        for image_path, descriptions in image_dict.items()
        if any(search_term.lower() in description.lower() for description in descriptions)
    ]

    # Define CSS class (assuming you have a style.css file linked)
    st.markdown(f"<link rel='stylesheet' href='path/to/your/style.css'>", unsafe_allow_html=True)

    # Display images with descriptions and file paths
    for image_path, descriptions in filtered_images:
        st.image(Image.open(image_path))
        st.markdown(f"<p class='caption-center'>Image Path: {image_path}</p>", unsafe_allow_html=True)
        for description in descriptions:
            st.markdown(f"<p class='caption-center'>Description: {description}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

