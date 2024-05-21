import os
import streamlit as st
def set_environment():
     os.environ["OPENAI_API_KEY"] == st.secrets["OPENAI_API_KEY"],
