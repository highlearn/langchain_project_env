from langgraph.graph import StateGraph, END
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from typing import TypedDict, Annotated, List
import operator