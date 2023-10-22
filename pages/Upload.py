import cv2
import streamlit as st
import numpy as np
import pytesseract
import requests

def chat_with_gpt(input_string):
    api_key = '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'  # Replace with your actual API key
    url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    data = {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': input_string}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"



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
        image = cv2.imread(image)
    else:
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Perform OCR
    text = pytesseract.image_to_string(preprocessed_image)
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

    input_string = "How can I write a Python function?"
    output = chat_with_gpt("given the raw text information from a reciept, could you seperaterate purchases into groups and recognize the store the its purchased from in a json file format. absolutely, always, please make sure that the json file only includes the purchases, with NO additional info. Only have a json file, no other words.")
    st.write(output)
