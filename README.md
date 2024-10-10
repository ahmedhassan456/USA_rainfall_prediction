# 🌦️ USA Rainfall Prediction 🌦️

This repository contains a machine learning project aimed at predicting whether it will rain tomorrow based on daily weather data from 20 major cities in the USA during the years 2024-2025. The model achieved an impressive **100% accuracy** and has been deployed using **FastAPI** and **Docker**. The Docker image is publicly available on Docker Hub.

## Project Overview

The dataset provides weather attributes crucial for predicting rainfall, including temperature, humidity, wind speed, cloud cover, and atmospheric pressure. This model can be useful in weather forecasting applications and for exploring weather trends.

### Features in the dataset:
- **Date**: The day the data was recorded.
- **Location**: The geographical area where the data was collected.
- **Temperature**: The average temperature of the day.
- **Humidity**: The percentage of moisture in the air.
- **Wind Speed**: The speed of the wind on that day.
- **Precipitation**: The amount of rainfall.
- **Cloud Cover**: The proportion of sky covered by clouds.
- **Pressure**: The atmospheric pressure.
- **Rain Tomorrow**: A binary label (1 = Yes, 0 = No), predicting if it will rain the next day.

## Model Performance

- **Accuracy**: 100%
- **Model**: The model uses machine learning techniques to predict whether it will rain tomorrow based on the given features.

## Project Structure

```bash
.
├── My_App/                      # Floder containing the API and Depolyment files
├── Test Model/                  # Floder containing model development and the Data
├── Dockerfile                   # Docker configuration for creating container
├── requirements.txt             # Text File containing require libraries
└── README.md                    # Project documentation (this file)
```
