from fastapi import FastAPI
import pickle
import uvicorn
from pydantic import BaseModel
import joblib
app = FastAPI()



class Predicted_inpt(BaseModel):
    Distance_to_the_nearest_MRT_station:float
    Number_of_convenience_stores:int
    Latitude:float
    Longitude:float

model = joblib.load('Real_Estate_Price_Prediction_new.pkl')


@app.get('/')
def testing_api():
    return {'message': 'Salam Barbarosa!'}


@app.post('/predicted_price')
def predicted_price(data:Predicted_inpt):
    features = [[data.Distance_to_the_nearest_MRT_station,data.Number_of_convenience_stores,data.Latitude,data.Longitude]]
    prediction = model.predict(features)
    return {'predicted price': prediction[0]}
