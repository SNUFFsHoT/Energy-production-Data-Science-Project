# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import numpy as np 
import pandas as pd
import pickle

pickle_in = open('D:/raj/Data Science Assignments/Turbines_Energy_Production/regressor_r.pkl' , 'rb')
regressor_r = pickle.load(pickle_in)

def predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity):


    prediction = regressor_r.predict([[temperature,exhaust_vacuum,amb_pressure,r_humidity]])
    print(prediction)
    return prediction
    
def main():
    st.title('Energy Predictor')
    html_temp = """
    <div style = 'background-color:tomato;padding:10px'>
    <h2  style = 'color:white;text-align:center;'>Energy Predictor App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    temperature = st.text_input("temperature","Type Here")
    exhaust_vacuum	= st.text_input("exhaust_vacuum","Type Here")
    amb_pressure = st.text_input("amb_pressure","Type Here")
    r_humidity = st.text_input("r_humidity","Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_energy_production(temperature,exhaust_vacuum,amb_pressure,r_humidity)
    st.success('The output is{}'. format(result))
    
    
if __name__ == '__main__':
    main()