import streamlit as st
import pandas as pd

st.title('CAR PREDICTION')
st.write("This model predicts car price using below features.")

df=pd.read_csv('car_prediction_cleaned.csv')
df.head()
