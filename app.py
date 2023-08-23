import streamlit as st

import os

#Initiating OPENAI API KEY
OPENAI_API_KEY == st.secrets(["OPENAI"]["OPENAI_API_KEY"])
 
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

import openai
from embedchain import App

#Initiating the Embedchain

allende_bot = App()

#embed Online resources
allende_bot.add("https://www.marxists.org/espanol/allende/")

# Set up Streamlit input and output 
st.title('Allende')
user_query = st.text_input("Enter your question about Elon Musk")
if st.button('Ask'):
    response = allende_bot.query(user_query)
    st.write(response)
