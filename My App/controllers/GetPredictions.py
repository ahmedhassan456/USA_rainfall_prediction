
def GetPredictions(model, encoder, inputs: list):
    result = {
        0: "Not Rainy",
        1: "Rainy",
    }

    inputs[1] = encoder.transform([inputs[1]])

    Temp_Humidity_Interaction = inputs[2] * inputs[3]
    Wind_Cloud_Ratio = inputs[4] / inputs[6]
    Year = inputs[0].dt.year
    Month = inputs[0].dt.month
    Day = inputs[0].dt.day

    inputs.append(Temp_Humidity_Interaction)
    inputs.append(Wind_Cloud_Ratio)
    inputs.append(Year)
    inputs.append(Month)
    inputs.append(Day)

    del inputs[0]

    predictions = model.predict([inputs])[0]

    return result[predictions]

    