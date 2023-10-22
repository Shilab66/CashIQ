import streamlit as st
import pytesseract
from PIL import Image, ImageOps, ImageFilter

def extractText(uploaded_file):
    # Convert the uploaded file to an image
    image = Image.open(uploaded_file)

    # Convert to grayscale
    gray_image = ImageOps.grayscale(image)

    # Apply Gaussian blur to reduce noise
    blurred_image = gray_image.filter(ImageFilter.GaussianBlur(radius=2))

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(blurred_image)

    return text

#Writes the title of the page
st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# If user attempts to upload a file.
if uploaded_file is not None:
    text = extractText(uploaded_file)
    st.write(f"Extracted text:\n{text}")
