# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from hugchat import hugchat
# # from hugchat.login import Login

# # #st.success("Select a Page")
# # nav_options = ["Home", "About", "Contact"]
# # choice = st.selectbox("", nav_options, label_visibility="hidden")

# # # Display content based on the selected option
# # if choice == "Home":
# #     st.title("Welcome to the Home Page")
# #     # Add content for the Home page
# # elif choice == "About":
# #     st.title("About Us")
# #     # Add content for the About page
# # elif choice == "Contact":
# #     st.title("Contact Us")
# #     # Add content for the Contact page


# # # Load example data
# # df = pd.DataFrame({
# #     'x': [1, 2, 3, 4],
# #     'y': [4, 7, 1, 5]
# # })

# # # Scatter Plot
# # st.header("Scatter Plot")

# # selected_product = st.selectbox(label="Select Product:", options=[1, 2, 3])
# # selected_start_date = st.date_input("Start Date:")
# # selected_end_date = st.date_input("End Date:")

# # df.index = pd.to_datetime(df.index)

# # selected_start_date = pd.to_datetime(selected_start_date)
# # selected_end_date = pd.to_datetime(selected_end_date)

# # query = f"index >= '{selected_start_date}' and index <= '{selected_end_date}'"
# # df_filtered = df.query(query)

# # fig_scatter = px.scatter(df_filtered, x='x', y='y', title='Scatter Plot')
# # st.plotly_chart(fig_scatter, use_container_width=True)

# # # Area Chart
# # st.header("Area Chart")
# # fig_area = px.area(df, x='x', y='y', title='Area Chart')
# # st.plotly_chart(fig_area, use_container_width=True)

# # user_input = st.sidebar.text_input("Enter your message:")

# # with st.sidebar:
# #     st.sidebar.header("Chatbot")
# #     if user_input:
# #     # Add your chatbot logic here
# #     # You can use an external library or define a function to handle the chatbot responses
# #     # For simplicity, let's echo back the user's input for now
# #         if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
# #             st.success('HuggingFace Login credentials already provided!', icon='✅')
# #             hf_email = st.secrets['EMAIL']
# #             hf_pass = st.secrets['PASS']
# #         else:
# #             hf_email = st.text_input('Enter E-mail:', type='password')
# #             hf_pass = st.text_input('Enter password:', type='password')
# #             if not (hf_email and hf_pass):
# #                 st.warning('Please enter your credentials!', icon='⚠️')
# #             else:
# #                 st.success("Please enter question.")
# #     st.sidebar.text(f"User: {user_input}")
# #     st.sidebar.text("Chatbot: " + user_input)

# # for message in st.session_state.messages:
# #     with st.chat_message(message["role"]):
# #         st.write(message["content"])

# # #Upload Files
# # st.header("Upload Files")
# # uploaded_file = st.file_uploader("Choose a file")
# # if uploaded_file is None:
# #     st.info(" Upload a file through config", icon="ℹ️")
# #     st.stop()

# import streamlit as st
# st.title("Main Page")
# st.sidebar.success("Select a page")

# st.sidebar.success("Insights")

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Business Insights
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
"""
)