import streamlit as st
from langchain import OpenAI
import os

#App title
st.set_page_config(page_title="test chatbot")

#Credentials
with st.sidebar:
  st.title('test chatbot')
