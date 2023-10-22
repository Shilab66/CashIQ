import cv2
import streamlit as st
from PIL import Image
import pytesseract
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

def ocr(image):
    # Open the image
    if isinstance(image, str):
        image = Image.open(image)
        image = cv2.imread(image)
    else:
        image = Image.open(image)
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    text = pytesseract.image_to_string(image)
    # Perform OCR
    text = pytesseract.image_to_string(preprocessed_image)
    return text

st.title("# Upload")
