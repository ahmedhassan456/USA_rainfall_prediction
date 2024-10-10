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
- **Hyperparameter Tuning**: The model's hyperparameters were tuned using **Optuna**, a popular framework for optimizing hyperparameters in machine learning.

## Project Structure

```bash
.
├── My_App/                      # Floder containing the API and Depolyment files
├── Test Model/                  # Floder containing model development and the Data
├── Dockerfile                   # Docker configuration for creating container
├── requirements.txt             # Text File containing require libraries
└── README.md                    # Project documentation (this file)
```

## Getting Started

### Prerequisites

To run this project locally, you will need the following tools installed on your machine:

- **Python 3.8+**
- **Docker**

### Local Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ahmedhassan456/USA_rainfall_prediction.git
   cd USA_rainfall_prediction
   ```

2. **Create a virtual environment and install dependencies**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application**:

   ```bash
   cd My_App
   python app.py
   ```

4. **Access the API**:

   Visit `http://localhost:8000/docs` to view the FastAPI Swagger UI and test the API.

### Docker Setup

The project can also be run using Docker.

1. **Pull the Docker image from Docker Hub**:

   ```bash
   docker pull ahmedsaqr28/rainfall_prediction:v1.0
   ```

2. **Run the Docker container**:

   ```bash
   docker run -it -p 8000:8000 ahmedsaqr28/rainfall_prediction:v1.0
   ```

3. **Access the API**:

   Visit `http://localhost:8000/docs` to interact with the API.


## Deployment

This project is deployed using Docker and FastAPI. The Docker image has been pushed to Docker Hub and can be pulled using the following command:

```bash
docker pull ahmedsaqr28/rainfall_prediction:v1.0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
