import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls["GROQ_API_KEY"]
            selected_groq_model = self.user_controls["selected_groq_model"]
            if groq_api_key=='' and os.getenv('GROQ_API_KEY') is None:
                st.error("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            llm = ChatGroq(
                model=selected_groq_model,
                api_key=groq_api_key,
            )

        except Exception as e:
            raise ValueError(f"Error in getting Groq LLM model: {e}")
        return llm