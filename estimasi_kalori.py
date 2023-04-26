import pickle
import streamlit as st

model = pickle.load(open('estimasi_kalori.sav', 'rb'))

st.title('Estimasi kalori bedasarkan item')

cal_fat = st.number_input('Input kalori')
total_fat  = st.number_input('Input total fat')
trans_fat= st.number_input('Input trans pat')

prediksi = ''
if st.button('Estimasi kalori bedasarkan item '):
    prediksi = model.predict(
        [[cal_fat, total_fat, trans_fat]]
    )
    st.write('Estimasi Kalori bedasarkan item : ', prediksi)