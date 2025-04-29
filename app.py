from fastapi import FastAPI
import joblib
from api.models import PredictRequest, PredictResponse

# Load the model
model = joblib.load("model.joblib")
label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    features = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = model.predict([features])[0]  # wrap in list for 2D array
    return PredictResponse(prediction=label_map[prediction])
