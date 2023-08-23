import streamlit as st
import openai
import os
from embedchain import App

#Initiating OPENAI API KEY
st.write(
    "Has environment variables been set:",
    os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"]

#Initiating the Embedchain

allende_bot = App()

#embed Online resources
allende_bot.add("https://www.marxists.org/espanol/allende/")

# Set up Streamlit input and output 
st.title('Allende')
user_query = st.text_input("Haz tu consulta")
if st.button('Ask'):
    response = allende_bot.query(user_query)
    st.write(response)
