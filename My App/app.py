from fastapi import FastAPI, Query
import uvicorn
from enum import Enum
from datetime import date, datetime
from controllers.LoadModel import LoadModel
from controllers.GetPredictions import GetPredictions

app = FastAPI()

model = LoadModel("My App/models/USA_rainfall_prediction_model_100%.pkl")
encoder = LoadModel("My App/models/encoder.pkl")

class Locations(str, Enum):
    New_York = "New York"
    Los_Angeles = "Los Angeles"
    Denver = "Denver"
    Seattle = "Seattle"
    San_Francisco = "San Francisco"
    Charlotte = "Charlotte"
    Indianapolis = "Indianapolis"
    Columbus = "Columbus"
    Jacksonville = "Jacksonville"
    Fort_Worth = "Fort Worth"
    Austin = "Austin"
    San_Jose = "San Jose"
    San_Diego = "San Diego"
    San_Antonio = "San Antonio"
    Philadelphia = "Philadelphia"
    Phoenix = "Phoenix"
    Houston = "Houston"
    Chicago = "Chicago"
    Washington_D_C = "Washington D.C."

@app.get("/")
def root():
    return {"Test": "Hello, World"}

@app.get("/USA Rainfall Prediction")
def predict(location: Locations,temperature: float = Query(..., ge=30.0, le=100.0),
            humidity: float = Query(..., ge=20.0, le=100.0), wind_speed: float = Query(..., ge=0.0, le=30.0), 
            precipitation: float = Query(..., ge=0.0, le=3.0), cloud_cover: float = Query(..., ge=10.0, le=100.0), 
            pressure: float = Query(..., ge=970.0, le=1040.0), year: int = Query(..., ge=2024, le=2030), 
            month: int = Query(..., ge=1, le=12), day: int = Query(..., ge=1, le=30)):
    
    temp_humidity_interaction = temperature * humidity
    wind_cloud_ratio = wind_speed / cloud_cover

    inputs = [location, temperature, humidity,
             wind_speed, precipitation, cloud_cover, 
             pressure, temp_humidity_interaction, wind_cloud_ratio,
             year, month, day]
    
    prediction = GetPredictions(model, encoder, inputs)

    return {"The Day is": prediction}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)