import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
with open('Real_Estate_Price_Prediction_new.pkl', 'rb') as file:
    model = pickle.load(file)

# Define labels for the input fields
labels = ['Distance_to_the_nearest_MRT_station', 'Number_of_convenience_stores', 'Latitude', 'Longitude']

def prediction(distance, num_stores, latitude, longitude):
    try:
        # Create a feature array for the model
        features = np.array([[distance, num_stores, latitude, longitude]])
        # Make a prediction
        price = model.predict(features)
        return price[0]
    except Exception as e:
        return f"Error in prediction: {e}"

# Streamlit UI
st.title("Real Estate Price Prediction")

# HTML for custom heading
html_temp = """ 
<div style ="background-color:yellow;padding:13px"> 
<h1 style ="color:black;text-align:center;">Real Estate Price Prediction App</h1> 
</div> 
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.header("Enter the details to predict the real estate price:")

# Input fields
distance = st.number_input('Distance to the nearest MRT station (meters)', min_value=0)
num_stores = st.number_input('Number of convenience stores', min_value=0)
latitude = st.number_input('Latitude')
longitude = st.number_input('Longitude')

# Predict button
if st.button('Predict'):
    result = prediction(distance, num_stores, latitude, longitude)
    st.write(f'The predicted price of the real estate is: {result}')
