import pickle
import streamlit as st

#Membaca Model Prediksi
Prediksi_kualitas = pickle.load(open('Susu_model.sav', 'rb'))

#judul web
st.title('Prediksi Kualitas Susu')

col1, col2 = st.columns (2)

# Definisi variabel
with col1 :
    pH = st.number_input("Masukkan nilai pH:")
with col2 :
    Temprature = st.slider("Pilih suhu (Temprature):", min_value=0, max_value=100, value=25)
with col1 :
    Taste = st.radio("Pilih rasa (Taste):", [0, 1])
with col2 :
    Odor = st.radio("Pilih bau (Odor):", [0, 1])
with col1 :
    Fat_Lemak = st.radio("Pilih lemak (Fat_Lemak):", [0, 1])
with col2 :
    Turbidity = st.radio("Pilih kekeruhan (Turbidity):", [0, 1])
with col1 :
    Colour = st.slider("Pilih warna (Colour):", min_value=0, max_value=255, value=128)

#code untuk prediksi
prediksi = ''

# Tombol Prediksi
if st.button('Prediksi Kualitas Susu'):
    # Lakukan prediksi
    milk_prediction = Prediksi_kualitas.predict([[pH, Temprature, Taste, Odor, Fat_Lemak, Turbidity, Colour]])

    # Tentukan hasil prediksi
    if milk_prediction[0] == 0:
        prediksi = "High"
    elif milk_prediction[0] == 1:
        prediksi = "Low"
    else :
        prediksi = 'Medium'

    # Tampilkan hasil prediksi
    st.success(f"Prediksi Kualitas Susu: {prediksi}")