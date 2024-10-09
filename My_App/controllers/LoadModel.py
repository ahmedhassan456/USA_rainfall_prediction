import pickle

def LoadModel(model_path:str):

    with open(model_path, "rb") as file:
        loaded_model = pickle.load(file)

    return loaded_model