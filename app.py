import streamlit as st
import pickle

# Load model
with open('sentimenmodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Judul aplikasi
st.title("Aplikasi Analisis Sentimen")
st.subheader("Masukkan teks untuk mengetahui sentimennya")

# Input dari pengguna
user_input = st.text_area("Masukkan teks di sini:")

if st.button("Analisis"):
    if user_input.strip() != "":
        # Prediksi
        prediction = model.predict([user_input])[0]
        st.write(f"Sentimen: **{prediction}**")
    else:
        st.write("Silakan masukkan teks terlebih dahulu.")
