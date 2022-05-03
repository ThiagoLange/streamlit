# Import Package
import streamlit as st

# Create a Header
st.header('st.button')

# Define Conditionals statements
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')