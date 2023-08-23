import streamlit as st
import openai
import os
from embedchain.config import QueryConfig
from embedchain.embedchain import App
from string import Template
import wikipedia

#Initiating OPENAI API KEY
os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"]

#Initiating the Embedchain

allende_bot = App()

# Embed Wikipedia page
page = wikipedia.page("Salvador Allende")
allende_bot.add(page.content)

#embed Online resources
allende_bot.add("https://www.marxists.org/espanol/allende/")

# Example: use your own custom template with `$context` and `$query`
allende_bot = Template("""
        You are Salvador Allende, a Chilean-born president,
        widely ranked among the greatest and most influential politicians of all time.

        Use the following information about Salvador Allende to respond to
        the human's query acting as Salvador Allende.
        Context: $context

        Keep the response brief. If you don't know the answer, just say "Lo desconozco", don't try to make up an answer.

        Human: $query
        Salvador Allende:""")

query_config = QueryConfig(template=einstein_chat_template, system_prompt="You are Salvador Allende.")
queries = [
        "Where did you complete your studies?",
        "Why did you win presidency in Chile?",
        "Why did you kill yourself?",
]

# Set up Streamlit input and output 
st.title('Allende')
for query in queries:
    query = st.text_input("Haz tu consulta")
if st.button('Pregunta'):
    response = allende_bot.query(query, config=query_config)
    st.write(response)
