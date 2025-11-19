import matplotlib.pyplot as plt
import os
from joblib import load, dump

def best_model(path):
    biggest_score = 0
    best_model = ""
    for artefact_name in os.listdir(path):
        if artefact_name != ".ipynb_checkpoints":
            score = int(artefact_name[-4:])
            if score > biggest_score:
                biggest_score = score
                best_model = artefact_name
    path_best_model = path + best_model
    model = load(path_best_model)
    return model
            

def prediction_digit(model, image):    
    return model.predict(image)
            
