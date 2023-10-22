import numpy as np
import streamlit as st
import pytesseract
from PIL import Image, ImageOps, ImageFilter
import easyocr

def extractText(uploaded_file, ):
    # Convert the uploaded file to an image
    image = Image.open(uploaded_file)

    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Perform OCR on the image
    results = reader.readtext(np.array(image))

    # Extract text from the results
    text = ' '.join([result[1] for result in results])

    return text

#Writes the title of the page
st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# If user attempts to upload a file.
if uploaded_file is not None:
    text = extractText(uploaded_file)
    st.write(f"Extracted text:\n{text}")
