import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image
from io import BytesIO

def extractText(uploaded_file):
    # Convert the uploaded file to an image
    image = Image.open(uploaded_file)

    #Adds gray scale to the image
    gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Apply adaptive thresholding to handle varying lighting conditions
    thresholded_image = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # Denoise the image using a median blur
    denoised_image = cv2.medianBlur(thresholded_image, 3)


    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(denoised_image)

    return text

#Writes the title of the page
st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# If user attempts to upload a file.
if uploaded_file is not None:
    text = extractText(uploaded_file)
    st.write(f"Extracted text:\n{text}")
