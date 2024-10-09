import numpy as np

def GetPredictions(model, encoder,inputs: list):
    result = {
        0: "Not Rainy",
        1: "Rainy",
    }

    inputs[0] = encoder.transform([inputs[0]])[0]

    predictions = model.predict([inputs])[0]

    return result[predictions]

    