# Import Packages
import streamlit as st

# Title
st.title('Customizing the theme of Streamlit apps')

# Text
st.write('Contents of the `.streamlit/config.toml` file of this app')

# Code Customize
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

