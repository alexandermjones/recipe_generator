# Standard library imports
import os

# Third party imports
from textgenrnn import textgenrnn

# Train model and generate new recipes
path = os.path.join("datasets", "bbcgoodfood.txt")
#textgen = textgenrnn()
#textgen.train_from_file(path, num_epochs=5, save_epochs=1, name="recipes")
textgen = textgenrnn('textgenrnn_weights.hdf5')
print(textgen.generate(5, temperature=0.5, return_as_list=True, prefix="Chocolate cake"))
#textgen.generate(interactive=True, temperature=0.5)