from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, Annotated, List
import operator

# --- 1. Define the Graph State ---
# The state contains all messages in our conversation history
class AgentState(TypedDict):
    messages: Annotated[List[AIMessage | HumanMessage], operator.add]

# --- 2. Initialize the Local Model (Phi-3 from Ollama) ---
# This connects to the 'ollama run phi3' process running locally
llm = ChatOllama(model="phi3", temperature=0.5)