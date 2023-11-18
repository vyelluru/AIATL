import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# Set up the Streamlit app title and description
st.title("Streamlit Page")

# Load example data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 5]
})

# Scatter Plot
st.header("Scatter Plot")
fig_scatter = px.scatter(data, x='Category', y='Values', title='Scatter Plot')
st.plotly_chart(fig_scatter, use_container_width=True)

# Area Chart
st.header("Area Chart")
fig_area = px.area(data, x='Category', y='Values', title='Area Chart')
st.plotly_chart(fig_area, use_container_width=True)


st.sidebar.header("Chatbot")
user_input = st.sidebar.text_input("Enter your message:")
if user_input:
    # Add your chatbot logic here
    # You can use an external library or define a function to handle the chatbot responses
    # For simplicity, let's echo back the user's input for now
    st.sidebar.text(f"User: {user_input}")
    st.sidebar.text("Chatbot: " + user_input)

#Upload Files
st.header("Upload Files")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()
    