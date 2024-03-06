import streamlit as st
import os
from PIL import Image

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

    # Get filtered list of images
    supported_extensions = [".jpg", ".jpeg", ".png"]
    image_list = [
        os.path.join(dir_path, f)
        for f in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, f))
        and os.path.splitext(f)[1].lower() in supported_extensions
    ]

    # Add search bar
    search_term = st.text_input("Search images:")

    # Filter images based on search term
    filtered_images = [
        image_path for image_path in image_list if search_term.lower() in os.path.basename(image_path).lower()
    ]

    # Sort images alphabetically
    filtered_images.sort()

    # Display images in grid layout
    num_cols = 4  # Adjust the number of columns as desired
    for i, image_path in enumerate(filtered_images):
        if i % num_cols == 0:
            # Create a new row after every `num_cols` images
            col1, col2, col3, col4 = st.columns(num_cols)
        image = Image.open(image_path)
        if i % num_cols == 0:
            col1.image(image)
        elif i % num_cols == 1:
            col2.image(image)
        elif i % num_cols == 2:
            col3.image(image)
        else:
            col4.image(image)

if __name__ == "__main__":
    main()

