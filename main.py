import os
import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import requests
import json
from predict import prediction
from flask import Flask, request

#Load Dataframe
path_kernel = "submission_kernel02.csv"
path_df = "train.csv"
dataframe2 = pd.read_csv(path_kernel)
dataframe1 = pd.read_csv(path_df)

class User_input(BaseModel):
    ID : int
        
app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/credit/<id_input>', methods=['GET'])
def credit(id_input):

    #récupération id client depuis argument url
    id_input = request.args.get('ID Client', default=1, type=int)
    
    #DEBUG
    print('id_client : ', id_input)
    print('shape df ', dataframe.shape)
    
    #calcul prédiction défaut et probabilité de défaut
    proba = prediction(id_input, dataframe2)

    dict_final = { 'proba' : float(proba[0][0]) }

    return jsonify(dict_final)   

#lancement de l'application
if __name__ == "__main__":
    app.run(debug=True)