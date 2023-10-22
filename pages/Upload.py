import streamlit as st
from io import BytesIO
import textract

def extractText(uploaded_file, ):
    #Convert the uploaded file to bytes
    file_content = uploaded_file.read()

    # Use textract to extract text
    text = textract.process(BytesIO(file_content))
    text = text.decode('utf-8')

    return text

#Writes the title of the page
st.write("# Upload a receipt")

# Initialize a streamlit file uploader widget.
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

# If user attempts to upload a file.
if uploaded_file is not None:
    text = extractText(uploaded_file)
    st.write(f"Extracted text:\n{text}")
