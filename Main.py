import streamlit as st
import plotly.express as px
import json

# Define the path to the JSON file
datafile = 'data.json'

# Read the data from the JSON file
with open(datafile, 'r') as file:
    data = json.load(file)

storeList = {}
categoryList = {}

for value in data.values():  # Iterate over the values of the dictionary
    store = value["store"]
    purchases = value["purchases"]

    if store in storeList:
        storeList[store] += 1
    else:
        storeList[store] = 1

    for i in purchases:
        category = i["category"]

        if category in categoryList:
            categoryList[category] += 1
        else:
            categoryList[category] = 1

col1A, col2A = st.columns(2)

with col1A:
    st.plotly_chart(px.pie(names=list(categoryList.keys()), values=list(categoryList.values()), title='Category'))

with col2A:
    max_value = max(categoryList.values())
    max_key = [key for key, value in categoryList.items() if value == max_value]
    st.write("Most Common Category: " + max_key[0])  # Access the first element

