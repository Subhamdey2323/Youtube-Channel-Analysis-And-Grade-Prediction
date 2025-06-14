# from flask import Flask, request, render_template
# import pickle
# import numpy as np

# # Load the model and encoder
# model = pickle.load(open('model.pkl', 'rb'))
# le = pickle.load(open('label_encoder.pkl', 'rb'))

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Extract values from form
#         uploads = float(request.form['uploads'])
#         subscribers = float(request.form['subscribers'])
#         views = float(request.form['views'])

#         # Prepare input for prediction
#         features = np.array([[uploads, subscribers, views]])
#         prediction = model.predict(features)
#         predicted_grade = le.inverse_transform(prediction)[0]

#         return render_template('index.html', prediction_text=f'Predicted Channel Grade: {predicted_grade}')
#     except Exception as e:
#         return render_template('index.html', prediction_text=f'Error: {str(e)}')

# if __name__ == '__main__':
#     app.run(debug=True)


import streamlit as st
import pickle
import numpy as np

# Load model & label encoder
model = pickle.load(open('model.pkl', 'rb'))
le = pickle.load(open('label_encoder.pkl', 'rb'))

# Set Streamlit page config
st.set_page_config(page_title="YouTube Channel Grade Predictor", layout="centered")

# Title
st.title("📊 YouTube Channel Grade Predictor")
st.write("Enter the channel's metrics below to predict its grade.")

# Input fields
uploads = st.number_input("Video Uploads", min_value=0, step=1)
subscribers = st.number_input("Subscribers", min_value=0, step=1)
views = st.number_input("Video Views", min_value=0, step=1)

# Prediction button
if st.button("Predict Grade"):
    try:
        # Prepare input
        features = np.array([[uploads, subscribers, views]])
        prediction = model.predict(features)
        predicted_grade = le.inverse_transform(prediction)[0]

        # Display result
        st.success(f"🎯 Predicted Channel Grade: **{predicted_grade}**")
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")