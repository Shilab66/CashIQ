import os
import cv2
import streamlit as st
from PIL import Image
import pytesseract
import numpy as np
import openai

# Set your API key here
api_key = st.secrets["OPENAI_KEY"]

# Initialize OpenAI API client
openai.api_key = api_key

def chat_with_gpt(input_text):
    response = openai.Completion.create(
        engine="davinci",  # You can use "davinci" or "text-davinci-003" as the engine.
        prompt=input_text,
        max_tokens=100  # Adjust this value to limit the length of the response.
    )
    return response.choices[0].text.strip()


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

def ocr_func(image):
    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Perform OCR
    text = pytesseract.image_to_string(preprocessed_image)
    return text

#Takes the ocr and runs it with ab incoming stream
def ocr_from_stream(file_stream):
    pil_image = Image.open(file_stream)
    image = np.array(pil_image)
    return ocr_func(image)

#write the title
st.title("# Upload")

#file upload component
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Perform OCR
    text = ocr_from_stream(uploaded_file)

    st.write(f"**Extracted Text:**\n\n{text}")

    user_input = "What is the capital of France?"
    response = chat_with_gpt(user_input)
    print(response)
