# Standard library imports
import os

# Third party imports
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
# train_model_on_data(os.path.join("data", "breakfast.txt"))
# train_model_on_data(os.path.join("data", "dinner.txt"))

textgen = textgenrnn(os.path.join("models", "dinner.hdf5"))
recipes = textgen.generate(20, temperature=0.5, return_as_list=True)
[print(recipe) for recipe in recipes]