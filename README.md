# YUM Recipe Generator
A neural network for generating new recipe titles.

## Description

Not sure what to eat?  
You've eaten literally everything on [BBC Good Food](https://www.bbcgoodfood.com/)
and want something similar to eat?
The idea of an AI choosing your food is a _recipe_ for excitement, not (just) horror?

Why not give YUM (Your Unique Meal-planner) a try!

![Example Gif](Animation.gif)

**Disclosure** There is _no_ guarantee that any meal suggested will be
edible, let alone tasty!

## Installation

```
pip3 install -r requirements.txt
```

Note that this project requires textgenrnn. This can be installed from PyPI, 
but as of writing this, the PyPI version is not up to date and it is recommended
to install from git instead as in the requirements file.

## Usage

Launch the Flask application and browse to `http://127.0.0.1:5000`.
Click on a meal type to discover your next meal!
To launch the application, simply enter:
```
python3 application.py
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

It is recommended to train models on `similar' recipes (as those split by meals are)
as otherwise very unpalatable combinations can occur.

## Contributing
Contributions are welcome, but please get in touch with me first
to discuss.

## License
[MIT](https://choosealicense.com/licenses/mit/)