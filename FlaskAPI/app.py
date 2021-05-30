import flask
from flask import Flask, jsonify, request
import json
#from data_input import data_in
import numpy as np
import pickle

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


app = Flask(__name__)

@app.route('/')
def hello_world():
    test_input = np.array([[10,0,0,1, 0, 0, 1, 0, 0, 0,0,2156,1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    model = load_models()
    preds = model.predict(test_input)
    preds_str = str(preds)
    return preds_str