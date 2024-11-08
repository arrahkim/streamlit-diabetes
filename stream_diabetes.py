import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

col1, col2 = st.columns(2)

# Input Nilai
with col1:
    Pregnancies = st.text_input('Input Nilai Pregnancies')
with col2:
    Glucose = st.text_input('Input Nilai Glucose')
with col1:
    BloodPressure = st.text_input('Input Nilai Blood Pressure')
with col2:
    SkinThickness = st.text_input('Input Nilai Skin Thickness')
with col1:
    Insulin = st.text_input('Input Nilai Insulin')
with col2:
    BMI = st.text_input('Input Nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Input Nilai Diabetes Pedigree Function')
with col2:
    Age = st.text_input('Input Nilai Age')

# kode untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
    
st.success(diab_diagnosis)