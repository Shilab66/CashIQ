import streamlit as st
from deta import Deta

st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file")

# If user attempts to upload a file.
if uploaded_file is not None:
    st.image(uploaded_file)
