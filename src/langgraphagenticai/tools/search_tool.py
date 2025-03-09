from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Get the tools for the agent.
    """
    tools = TavilySearchResults(max_results=5,include_answer=True,
    include_raw_content=True,
    include_images=True)
    return[tools]

def create_tool_node(tools):
    """
    Create the tool node for the agent.
    """
    return ToolNode(tools=tools)