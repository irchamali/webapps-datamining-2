import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
from sklearn.naive_bayes import GaussianNB

st.title('Klasifikasi Penguin menggunakan Algoritma Naive Bayes')

st.write(""" 
Aplikasi berbasis Web untuk memprediksi (mengklasifikasi) jenis penguin **Palmer Penguin**
Data yang didapat dari [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) dalam bentuk R oleh Allison Horst.
""")

img = Image.open('penguins.png')
img = img.resize((700, 418))
st.image(img, use_column_width=False)

img2 = Image.open('culmen_depth.png')
img2 = img2.resize((700, 450))
st.image(img2, use_column_width=False)
