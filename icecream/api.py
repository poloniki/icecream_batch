from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from icecream.model.prediction import regression_model

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def hellow_world():
    return {"greeting": "hellow world"}


@app.get("/predict")
def predict(temp: float, crowd: int):
    return {"prediction": regression_model(temp, crowd)}
