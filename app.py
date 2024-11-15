import numpy as np
import pandas as pd
import pickle 
import streamlit as st



model = pickle.load(open('model.pkl','rb'))

car_data = pd.read_csv('https://raw.githubusercontent.com/kambletejas218/car-prediction/refs/heads/main/car_prediction_cleaned.csv')

st.header('Car Price Prediction Model')

brand = st.selectbox('Select Car Brand', car_data['brand'].unique())
filtered = car_data[car_data['brand'] == brand]['model'].unique()
car_model = st.selectbox('Select Car Model',filtered)
transmission = st.radio('Select Car Transmission Type',car_data['transmission'].unique())
make_year = st.selectbox('Select Manufacturing Year ',car_data['make_year'].unique())
fuel_type = st.selectbox('Select Fuel Type',car_data['fuel_type'].unique())
engine_capacity = st.selectbox('Select Engine Capacity (CC)  ',car_data['engine_capacity(CC)'].unique())
km_driven = st.slider('Select Kilometer Driven ',float(car_data['km_driven'].min()),float(car_data['km_driven'].max()))
engine_capacity = st.number_input('Select Ownership',int(car_data['ownership'].min()),int(car_data['ownership'].max()))


# Predict Button
if st.button('Predict Price'):
    input_data_model = pd.DataFrame(
    [[brand,car_model,transmission,make_year,fuel_type,engine_capacity,km_driven,engine_capacity]],
    columns=['brand','model','transmission','make_year','fuel_type','engine_capacity(CC)','km_driven','ownership'])

    input_data_model['transmission'] = input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2])
    input_data_model['brand'] = input_data_model['brand'].replace(['Mahindra', 'Hyundai', 'Tata', 'Honda', 'Ford', 'Maruti', 'KIA',
       'MG', 'Renault', 'Volkswagen', 'Nissan', 'Skoda', 'Toyota',
       'Datsun', 'Jeep'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    
    input_data_model['model'] = input_data_model['model'].replace(['Thar', 'Verna', 'Harrier', 'City', 'Ecosport', 'WR-V', 'PUNCH',
       'NEXON', 'XUV700', 'Dzire', 'GRAND', 'Tiago', 'Creta', 'Alto',
       'Amaze', 'SELTOS', 'HECTOR', 'TIGOR', 'FREESTYLE', 'Ciaz',
       'Celerio', 'CARENS', 'IGNIS', 'TRIBER', 'XUV500', 'S', 'ALTROZ',
       'Xcent', 'Grand', 'XL6', 'Wagon', 'NEW', 'Baleno', 'VENUE',
       'VIRTUS', 'SONET', 'MAGNITE', 'Rapid', 'Swift', 'Ertiga', 'YARIS',
       'Go', 'KUV', 'Vitara', 'Kwid', 'Ameo', 'Redi', 'Jazz', 'Tucson',
       'TIAGO', 'Kiger', 'Safari', 'Polo', 'i20', 'URBAN', 'Compass',
       'XUV300', 'Glanza', 'Elite', 'Duster', 'Vento', 'New', 'AURA',
       'XCENT', 'Brio', 'Ritz', 'Etios', 'i10', 'BREZZA', 'Santro',
       'Bolero', 'Scorpio', 'Kuv100', 'BR-V', 'Eeco', 'Micra', 'Eon',
       'Innova', 'TUV300', 'Pulse', 'OMNI', 'KUSHAQ', 'A', 'TAIGUN',
       'Zest', 'Terrano', 'Nano', 'ALCAZAR', 'Civic', 'SLAVIA', 'Corolla'],
       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
        54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
        80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91])
    input_data_model['fuel_type'] = input_data_model['fuel_type'].replace(['Diesel', 'Petrol', 'CNG', 'Electric'],[1,2,3,4])

    car_price = model.predict(input_data_model)

    st.success(f'Estimated Price of the Car: ₹ {car_price[0]:,.2f}')
