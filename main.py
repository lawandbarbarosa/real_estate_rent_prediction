import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
pickle_in = open('real_estate_prediction.pkl', 'rb')
model = pickle.load(pickle_in)

# Define labels for the input fields
labels = ['Distance_to_the_nearest_MRT_station', 'Number_of_convenience_stores', 'Latitude', 'Longitude']

def prediction(distance, num_stores, latitude, longitude):
    # Ensure inputs are in the correct format (as numpy array) if needed
    inputs = np.array([[distance, num_stores, latitude, longitude]])
    prediction = model.predict(inputs)
    return prediction[0]  # Return the predicted value

def main():
    # Set the title of the app
    st.set_page_config(page_title="Real Estate Price Prediction App", page_icon="🏡")
    
    # Enhanced HTML for the title section with an image
    html_temp = """ 
    <style>
    .main-title {
        background-color: #FFC300;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .main-title h1 {
        color: #000000;
        font-family: Arial, sans-serif;
    }
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .image-container img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .input-section {
        background-color: #f2f2f2;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .input-section label {
        font-family: Arial, sans-serif;
        font-size: 16px;
    }
    .input-section input {
        margin-bottom: 10px;
    }
    .prediction-result {
        font-family: Arial, sans-serif;
        font-size: 18px;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    <div class="main-title"> 
        <h1>Real Estate Rent Prediction</h1> 
    </div>
    <div class="image-container">
        <img src="https://th.bing.com/th/id/OIP.kINwqVgvCEYzGUOcI2RKCgHaE8?rs=1&pid=ImgDetMain.jpg" alt="Real Estate Image">
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Input section with enhanced styling
    with st.container():
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
        
        distance = st.number_input('Distance to the nearest MRT station (meters)', min_value=0)
        num_stores = st.number_input('Number of convenience stores', min_value=0)
        latitude = st.number_input('Latitude')
        longitude = st.number_input('Longitude')
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    result = ""

    # Predict button
    if st.button('Predict'):
        result = prediction(distance, num_stores, latitude, longitude)
        st.markdown(f'<div class="prediction-result">The predicted price of the real estate is: {result:.2f}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
