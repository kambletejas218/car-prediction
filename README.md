# 🚗 **Car Price Prediction Application**  

A **machine learning-powered** web application built with **Streamlit** for predicting car prices based on various features. 🚀  

---

## ✨ **Features**
✔️ Interactive UI for seamless car price predictions  
✔️ Predict based on car **brand**, **model**, **transmission type**, and more  
✔️ Powered by a **trained machine learning model**  
✔️ User-friendly interface with sliders and dropdowns  

---

## 🛠️ **How to Run the Application**  

### **📋 Prerequisites**
Make sure you have the following installed:  
- Python 3.8+ 🐍  
- Required libraries (install them via 'requirements.txt'):  
  - streamlit
  - pandas
  - numpy
  - scikit-learn

### **📂 Project Structure**
├── app.py                   # Streamlit app script <br>
├── car_prediction_cleaned.csv  # Cleaned dataset <br>
├── best_model.pkl           # Pre-trained machine learning model <br>
└── README.md                # Project documentation <br>

### **📊 Dataset Details**
**- The cleaned dataset contains the following columns:**

**🚗 Brand: Manufacturer of the car**
**🏷️ Model: Specific car model**
**⚙️ Transmission: Manual or Automatic**
**📅 Manufacturing Year: Year of production**
**⛽ Fuel Type: Diesel, Petrol, CNG, or Electric**
**🔧 Engine Capacity (CC): Engine power in cubic centimeters**
**📏 Kilometers Driven: Total distance driven**
**👤 Ownership: First, second, or third-hand ownership**

### **🤖 Model Information**
  **- The machine learning model (best_model.pkl) is trained using the dataset to predict car prices based on the above features. The model achieved 90% accuracy during training and testing, ensuring reliable price predictions. It preprocesses inputs by encoding categorical variables and scaling numerical features for optimal performance.**



