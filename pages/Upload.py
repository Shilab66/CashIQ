import streamlit as st
import ocr

#Writes the title of the page
st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# If user attempts to upload a file.
if uploaded_file is not None:
    text = ocr.extractText(uploaded_file)
    st.write(f"Extracted text:\n{text}")
