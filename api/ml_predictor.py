import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image


class PlantPredictor:
    def __init__(self, model_filename, class_names, image_size):
        # Get the directory of this module (ml_predictor.py)
        module_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(module_dir, model_filename)
        
        self.model = load_model(model_path)
        self.class_names = class_names
        self.image_size = image_size

    def preprocess_image(self, image):
        # Convert the Pillow Image to RGB format and preprocess it
        img_array = image.convert("RGB").resize(self.image_size)
        img_array = np.array(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize the pixel values
        return img_array

    def predict(self, image):
        # Preprocess the image
        preprocessed_image = self.preprocess_image(image)

        # Use the loaded model for prediction
        predictions = self.model.predict(preprocessed_image)

        # Get the class label with the highest probability
        predicted_class = np.argmax(predictions)

        # Map the class label to the plant species name using class_names
        predicted_species = self.class_names[predicted_class]

        return predicted_species
