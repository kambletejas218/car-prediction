import streamlit as st
import pandas as pd

st.title('CAR PREDICTION')
st.write("This model predicts car price using below features.")

df=pd.read_csv('https://github.com/kambletejas218/car-prediction/blob/main/car_prediction_cleaned.csv')
df.head()
