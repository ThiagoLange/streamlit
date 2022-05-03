# Import Packages
import streamlit as st

# Header
st.header('st.selectbox')

# Example
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)

