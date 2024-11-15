import streamlit as st
import pandas as pd

st.title('CAR PREDICTION')
st.write("This model predicts car price using below features.")

with st.expander('Data'):
  st.write("**RAW DATA**")
  df=pd.read_csv('https://raw.githubusercontent.com/kambletejas218/car-prediction/refs/heads/main/car_prediction_cleaned.csv')
  df
