from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
import os



class ImageCaptioning:
    def __init__(self):
        self.model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        self.tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        self.max_length = 16
        self.num_beams = 4
        self.gen_kwargs = {"max_length": self.max_length, "num_beams": self.num_beams}
    
    def predict_caption(self, image_paths):
        images = []
        for image_path in image_paths:
            i_image = Image.open(image_path)
            if i_image.mode != "RGB":
                i_image = i_image.convert(mode="RGB")
            images.append(i_image)

        pixel_values = self.feature_extractor(images=images, return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(self.device)

        output_ids = self.model.generate(pixel_values, **self.gen_kwargs)

        preds = self.tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        preds = [pred.strip() for pred in preds]
        return preds

    @staticmethod
    def is_image(filename):
        try:
            img = Image.open(filename)
            img.close()
            return True
        except Exception as e:
            return False

    @staticmethod
    def get_images_in_directory(directory):
        
        image_paths = []
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if ImageCaptioning.is_image(filepath):
                image_paths.append(filepath)

        return image_paths

    def rename_file(self, image_path, new_name):
        if os.path.isfile(image_path):
            dirname = os.path.dirname(image_path)
            new_path = os.path.join(dirname, new_name)
            os.rename(image_path, new_path)
            return f"Renamed {image_path} to {new_path}"
        else:
            return f"Image {image_path} not found."

    def rename_directory(self, directory_path, new_name):
        image_paths = self.check_images_in_directory(directory_path)
        for image_path in image_paths:
            file_name, file_ext = os.path.splitext(os.path.basename(image_path))
            new_filename = f"{new_name}_{file_name}{file_ext}"
            self.rename_file(image_path, new_filename)


    def make_index(self):
       directory_path = "/home/dumball/pngs"
       image_paths = self.get_images_in_directory(directory_path)
       dictionary = {image_path: self.predict_caption([image_path]) for image_path in image_paths}
       return dictionary
    


    


