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

    for i in purchases:
        if store.lower() in storeList:
            storeList[store.lower()] += 1
        else:
            storeList[store.lower()] = 1

        category = i["category"]

        if category.lower() in categoryList:
            categoryList[category.lower()] += 1
        else:
            categoryList[category.lower()] = 1

st.write("## Dashboard")

max_value = max(categoryList.values())
max_key = [key for key, value in categoryList.items() if value == max_value]

st.write("## Most Common Category: " + max_key[0])  # Access the first element
st.plotly_chart(px.pie(names=list(categoryList.keys()), values=list(categoryList.values())))


max_value = max(storeList.values())
max_key = [key for key, value in storeList.items() if value == max_value]

st.write("## Most Common Store: " + max_key[0])  # Access the first element
st.plotly_chart(px.pie(names=list(storeList.keys()), values=list(storeList.values())))