import streamlit as st
import requests

st.header("Best app")
URL = "https://icecream-626932554468.europe-west1.run.app/predict"


def get_prediction(crowd, temp):
    response = requests.get(
        URL,
        params={"temp": temp, "crowd": crowd},
    )

    return response


crowd = st.number_input("Crowd")
temp = st.number_input("Temp")

button = st.button("Predict")

if button:
    result = get_prediction(int(crowd), temp)
    st.write(result)
    st.write(result.json())
    st.balloons()
