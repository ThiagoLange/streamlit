# Import Package
import streamlit as st

# Head
st.header('st.multiselect')

# Example
options = st.multiselect(
    'What are you favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)