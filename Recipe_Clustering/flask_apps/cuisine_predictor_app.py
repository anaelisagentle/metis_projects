from flask import request
import flask
#from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle
import pandas as pd

#---------- MODEL IN MEMORY ----------------#

# Read the scientific data on breast cancer survival,
# Build a LogisticRegression predictor on it
# patients = pd.read_csv("haberman.data.txt", header=None)
# patients.columns=['age','year','nodes','survived']
# patients=patients.replace(2,0)  # The value 2 means death in 5 years

# X = patients[['age','year','nodes']]
# Y = patients['survived']

with open("cluster.pkl", 'rb') as picklefile:
    clusters = pickle.load(picklefile)

with open("cuisine_titles.pkl", 'rb') as picklefile:
    titles = pickle.load(picklefile)

with open("cluster_df.pkl", 'rb') as picklefile:
    cluster_df = pickle.load(picklefile)


def similar_cuisines(cuisine, df, titles):
    
    similar_cuisines = []
    cluster = int(df[cuisine])
    
    for title in titles:
        cluster_compare = int(df[title])
        if cluster == cluster_compare:
            similar_cuisines.append(title)
    if cuisine == "vietnamese":
        similar_cuisines.append("korean")
    if cuisine == "mexican":
        similar_cuisines.append("brazilian")
    similar_cuisines.remove(cuisine)
    return(similar_cuisines)

input_cuisine = "british"

similar_cuisines(input_cuisine, cluster_df, titles)

#similar_cuisines(input_cuisine, cluster_df, titles)



#---------- URLS AND WEB PAGES -------------#

# Initialize the app
app = flask.Flask(__name__)

# Homepage
@app.route("/")
def viz_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("awesome.html", 'r') as viz_file:
        return viz_file.read()







# Get an example and return it's score from the predictor model
@app.route("/predict", methods=["POST"])
def predict():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    input_cuisine = request.form.get('myVal')
    similar_cuisines(input_cuisine, cluster_df, titles)
    #input_cuisine = data["exa
    return input_cuisine
    
    #score = similar_cuisines(input_cuisine, cluster_df, titles)
    # Put the result in a nice dict so we can send it as json
    #results = {"score": score}
    #return flask.jsonify(results)

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0')
app.run(debug=True)


