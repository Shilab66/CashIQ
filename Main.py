import streamlit as st
import pandas as pd

# Define the path to the JSON file
file_path = 'data.json'

# Load the JSON data into a pandas DataFrame
df = pd.read_json(file_path)

st.dataframe(df)