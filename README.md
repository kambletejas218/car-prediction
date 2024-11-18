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
├── app.py                    # Streamlit app script <br>
├── car_prediction_cleaned.csv   # Cleaned dataset <br>
├── best_model.pkl            # Pre-trained machine learning model <br>
└── README.md                 # Project documentation <br>

### **📊 Dataset Details**
**The cleaned dataset contains the following columns:**

 - 🚗 Brand: Manufacturer of the car <br>
 - 🏷️ Model: Specific car model <br>
 - ⚙️ Transmission: Manual or Automatic <br>
 - 📅 Manufacturing Year: Year of production <br>
 - ⛽ Fuel Type: Diesel, Petrol, CNG, or Electric <br>
 - 🔧 Engine Capacity (CC): Engine power in cubic centimeters <br>
 - 📏 Kilometers Driven: Total distance driven <br>
 - 👤 Ownership: First, second, or third-hand ownership <br>

### **🤖 Model Information**
  **- The machine learning model (best_model.pkl) is trained using the dataset to predict car prices based on the above features. The model achieved 90% accuracy during training and testing, ensuring reliable price predictions. It preprocesses inputs by encoding categorical variables and scaling numerical features for optimal performance.**

### **🌟 Acknowledgments**

**Thanks to the developers of:**

  - Streamlit for the interactive UI framework
  - Pandas & NumPy for data manipulation
  - Scikit-learn for the model training
