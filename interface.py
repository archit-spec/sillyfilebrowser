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
        (os.path.join(dir_path, f), os.path.basename(f))
        for f in os.listdir(dir_path)
        if os.path.isfile(os.path.join(dir_path, f))
        and os.path.splitext(f)[1].lower() in supported_extensions
    ]

    # Add search bar
    search_term = st.text_input("Search images:", "")

   # Filter images based on search term
   # filtered_images = [
   #     image_path_filename
   #     for image_path_filename in image_list
   #     if search_term.lower() in image_path_filename[1].lower()
   # ]


    image_features = [extract_image_features(path) for path in image_list]
    index = create_faiss_index(image_features)

    filtered_images = search_images(search_term, index, image_features, top_k=5)

    # Define CSS class (assuming you have a style.css file linked)
    st.markdown(f"<link rel='stylesheet' href='path/to/your/style.css'>", unsafe_allow_html=True)

    # Display images with filename
    columns = st.columns(2)  # Adjust the number of columns as desired
    for i, (image_path, filename) in enumerate(filtered_images):
        with columns[i % len(columns)]:
            image = Image.open(image_path)
            st.image(image)
            st.markdown(f"<p class='caption-center'>{filename}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

