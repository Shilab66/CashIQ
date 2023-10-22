import streamlit as st
from PIL import Image
import pytesseract

def ocr(image):
    text = pytesseract.image_to_string(image)
    return text

st.title("# Upload")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Perform OCR
    text = ocr(uploaded_file)

    st.write(f"**Extracted Text:**\n\n{text}")
