# Standard library imports
import os

# Third party imports
import tensorflow as tf
from textgenrnn import textgenrnn

def train_model_on_data(data_path: str):
    """
    """
    name = os.path.join("models", os.path.basename(data_path)[:-4])
    textgen = textgenrnn()
    textgen.train_from_file(data_path, num_epochs=5, save_epochs=1, name=name)
    textgen.save(weights_path=name+".hdf5")

# Uncomment to train a new model
# train_model_on_data(os.path.join("data", "dessert.txt"))
#train_model_on_data(os.path.join("data", "breakfast.txt"))
#train_model_on_data(os.path.join("data", "dinner.txt"))

def setup_models() -> textgenrnn:
    breakfast_model = textgenrnn(os.path.join("models", "breakfast.hdf5"))
    dinner_model = textgenrnn(os.path.join("models", "dinner.hdf5"))
    dessert_model = textgenrnn(os.path.join("models", "dessert.hdf5"))
    return breakfast_model, dinner_model, dessert_model

def get_recipe(model: textgenrnn) -> str:
    recipes = model.generate(1, temperature=0.4, return_as_list=True)
    return recipes[0]

breakfast_model = textgenrnn(os.path.join("models", "breakfast.hdf5"))
breakfast_model.model.config = breakfast_model.config
tf.keras.models.save_model(breakfast_model.model, 'breakfast.h5')