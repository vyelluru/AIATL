import streamlit as st
#We are using Claude
#from langchain.llms import OpenAI

st.title('App')

#openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# def generate_response(input_text):
#     llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
#     st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the best place for my product?')
    submitted = st.form_submit_button('Submit')
    #generate_response(text)