# 🌱 Crop Recommendation System Using Machine Learning

A Machine Learning based web application that recommends the most suitable crop based on soil and environmental conditions.

The system uses a **Random Forest Classifier** to predict the best crop by analyzing parameters such as Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Soil pH, and Rainfall.

---

# 📌 Project Overview

Agriculture depends heavily on soil quality and climatic conditions. Choosing the right crop is a difficult task for farmers because different crops require different environmental conditions.

This project provides an intelligent crop recommendation system that helps farmers select the most suitable crop using Machine Learning.

The application provides recommendations instantly through a simple and user-friendly web interface built using Flask and Bootstrap.

---

# 🎯 Objectives

- Predict the best crop based on soil and weather parameters.
- Use Machine Learning to assist farmers in decision making.
- Build a simple web-based crop prediction system.
- Provide accurate recommendations using Random Forest Algorithm.

---

# 🚀 Features

✅ Machine Learning based crop prediction  
✅ Random Forest Classifier  
✅ Flask Web Application  
✅ Bootstrap Responsive UI  
✅ Soil parameter analysis  
✅ Weather condition analysis  
✅ Prediction confidence percentage  
✅ User-friendly interface  

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Backend

- Flask

## Machine Learning

- Scikit-learn
- Random Forest Classifier

## Data Processing

- Pandas
- NumPy

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

# 🤖 Machine Learning Algorithm

## Random Forest Classifier

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to make accurate predictions.

Advantages:

- High accuracy
- Handles multiple classes
- Reduces overfitting
- Works well with agricultural datasets

---

# 📂 Dataset

Dataset Used:

**Crop Recommendation Dataset**

Dataset Features:

| Feature | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Temperature in Celsius |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall amount |
| Label | Recommended crop |

---

# 📁 Project Structure
Crop-Recommendation-System/

│
├── app.py
├── train_model.py
├── model.pkl
├── crop_recommendation.csv
├── requirements.txt
├── README.md
│
├── templates/
│ ├── base.html
│ ├── index.html
│ └── result.html
│
└── static/
├── css/
│ └── style.css
│
└── js/
└── script.js


---

# ⚙️ Installation and Setup

## Step 1: Clone or Download Project

Download the project folder.

---

## Step 2: Create Virtual Environment


python -m venv venv


Activate environment:

### Windows


venv\Scripts\activate


### Linux/Mac


source venv/bin/activate


---

## Step 3: Install Required Libraries

Run:


pip install -r requirements.txt

---

# 🧠 Train the Machine Learning Model

Before running the application, train the model.

Run:

python train_model.py


After successful training, a file will be created:

model.pkl


This file contains the trained Random Forest model.

---
# ▶️ Run the Flask Application

Start the server:


python app.py


The application will run on:


http://127.0.0.1:5000


Open the URL in your browser.

---

# 🖥️ How to Use

1. Enter soil nutrient values:
   - Nitrogen
   - Phosphorus
   - Potassium

2. Enter environmental conditions:
   - Temperature
   - Humidity
   - Soil pH
   - Rainfall

3. Click:

Predict Crop


4. The system will display:

- Recommended crop
- Prediction confidence

---

# 📊 Model Performance

The Random Forest model generally achieves high accuracy on the Crop Recommendation Dataset.

Performance depends on:

- Dataset quality
- Training/testing split
- Feature distribution