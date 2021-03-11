# Standard library imports
from flask import Flask, render_template, request
import requests

# Local imports
from recipes import setup_models, get_recipe

app = Flask(__name__)
breakfast_model, dinner_model, dessert_model = setup_models()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/breakfast')
def breakfast_suggestion():
    return get_recipe(breakfast_model)

@app.route('/dinner')
def dinner_suggestion():
    return get_recipe(dinner_model)

@app.route('/desserts')
def dessert_suggestion():
    return get_recipe(dessert_model)


if __name__ == '__main__':
    app.run(debug=True)