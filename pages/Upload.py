import cv2
import streamlit as st
from PIL import Image
import pytesseract
import numpy as np

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Noise Reduction
    denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)

    # Contrast Enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)

    return enhanced

def ocr_from_stream(file_stream):
    pil_image = Image.open(file_stream)
    image = np.array(pil_image)
    return ocr(image)

st.title("# Upload")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Perform OCR
    text = ocr_from_stream(uploaded_file)

    st.write(f"**Extracted Text:**\n\n{text}")
