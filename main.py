import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
from sklearn.naive_bayes import GaussianNB

# st.title('Klasifikasi Penguin menggunakan ALgoritma Naive Bayes')
st.write("""
# Klasifikasi penguin (Web Apps)
Aplikasi berbasis Web untuk memprediksi (mengklasifikasi) jenis penguin **Palmer Penguin**
Data yang didapat dari [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) dalam bentuk R oleh Allison Horst.
""")