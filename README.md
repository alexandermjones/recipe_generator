# Recipe Generator
A neural network for generating new recipe titles.

## Description

Not sure what to have to eat?  
You've eaten literally everything available in BBC Good Food and want something similar?  


This repository is currently in beta.

## Installation

This project requires textgenrnn as the only dependency. This can be installed from PyPI, 
but as of writing this (06/03/21) this version is not up to date and it is recommended
to install from git instead. The command for this is:
```
pip3 install git+git://github.com/minimaxir/textgenrnn.git
```

## Usage

TBD.
```
python3 
```

## Datasets

The original dataset for this is a compilation of BBC Good Food recipe data in JSON format, 
obtained from [here](https://github.com/mneedham/bbcgoodfood).
The file `clean_recipes.py` will generate the different recipe titles from this, available within the
data folder.

## Contributing
Contributions are welcome, but please get in touch with me first
to discuss.

## License
[MIT](https://choosealicense.com/licenses/mit/)