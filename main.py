import streamlit as st
import pickle
import numpy as np

# Load the pre-trained model
pickle_in = open('real_estate_prediction.pkl','rb')
model = pickle.load(pickle_in)

# Define labels for the input fields
labels = ['Distance_to_the_nearest_MRT_station', 'Number_of_convenience_stores', 'Latitude', 'Longitude']

def prediction(distance, num_stores, latitude, longitude):
    # Ensure inputs are in the correct format (as numpy array) if needed
    inputs = np.array([[distance, num_stores, latitude, longitude]])
    prediction = model.predict(inputs)
    return prediction[0]  # Return the predicted value

def main():

    st.title("Real Estate Price Prediction") 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Real Estate Price Prediction App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Streamlit UI
    distance = st.number_input('Distance to the nearest MRT station (meters)', min_value=0)
    num_stores = st.number_input('Number of convenience stores', min_value=0)
    latitude = st.number_input('Latitude')
    longitude = st.number_input('Longitude')
    result = ""

    # Predict button
    if st.button('Predict'):
        result = prediction(distance, num_stores, latitude, longitude)
        st.write(f'The predicted price of the real estate is: {result:.2f}')  # Display the result

if __name__=='__main__': 
    main()
