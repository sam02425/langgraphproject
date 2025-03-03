from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """A basic chatbot node for implementation."""
    def __init__(self,model):
        self.llm = model

    def process(self, state: State)-> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"message": self.llm(state.value["messages"])}