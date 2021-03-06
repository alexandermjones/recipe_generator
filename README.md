# YUM Recipe Generator
A neural network for generating new recipe titles.

## Description

Not sure what to eat?  
You've eaten literally everything on [BBC Good Food](https://www.bbcgoodfood.com/)
and want something similar to eat?
The idea of an AI choosing your food is a _recipe_ for excitement, not (just) horror?

Why not give YUM (Your Unique Meal-planner) a try!

**Disclosure** There is _no_ guarantee that any meal suggested will be
edible, let alone tasty!

## Installation

This project requires textgenrnn as the only dependency. This can be installed from PyPI, 
but as of writing this (06/03/21) the PyPI version is not up to date and it is recommended
to install from git instead. The command for this is:
```
pip3 install git+git://github.com/minimaxir/textgenrnn.git
```

## Usage

TBD.
```
python3 recipes.py
```

## Datasets

The original dataset for this is a compilation of BBC Good Food recipe data in JSON format, 
obtained from [here](https://github.com/mneedham/bbcgoodfood).
The file `clean_recipes.py` will generate the different recipe types from this, available within the
data folder.

## Models

There are four pre-trained models in this repository: `allrecipes.hdf5`,
`breakfast.hdf5`, `dessert.hdf5` and `dinner.hdf5`.
These models have been trained on the relevant datasets in the data folder.
If you wish to train new models, call the function `train_model_on_data` in `recipes.py`
on the relevant dataset.

## Contributing
Contributions are welcome, but please get in touch with me first
to discuss.

## License
[MIT](https://choosealicense.com/licenses/mit/)