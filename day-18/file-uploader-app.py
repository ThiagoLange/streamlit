# Import Packages
from distutils.command.upload import upload
import streamlit as st
import pandas as pd

# Title
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Dataframe')
    st.write(df)
    st.subheader('Descriptive Statitics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')

