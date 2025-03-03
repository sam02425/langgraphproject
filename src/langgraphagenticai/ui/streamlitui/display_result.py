import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stram({'messages':("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value["message"])
                    with st.chat_message("user"):
                        st.write(value["user_message"])
                    with st.chat_message("assistant"):
                        st.write(value["message"].content)
