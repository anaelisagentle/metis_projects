import flask
import pandas as pd
import numpy as np

# Initialize the app
app = flask.Flask(__name__)

# HTTP extension
@app.route("/")
def hello():
	return "Flask app works!"


@app.route("/predict", methods=["POST"])
def predict():
	df = pd.read_pickle("test.pkl")
	input_data = flask.request.json
	country = input_data["Country"]
	ingredients = list(df[country])

	results = {"Ingredients" : ingredients}

	return flask.jsonify(results)


app.run(debug=True)

