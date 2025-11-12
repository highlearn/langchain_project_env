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
# --- 3. Define the Nodes (Steps in the Graph) ---

def call_model(state):
    """
    Call the local LLM and return its response message.
    """
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# --- 4. Build the Graph ---

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)

# Set the entry point to be the 'agent' node
workflow.set_entry_point("agent")

# Every time the agent runs, it goes back to the agent (simple loop)
workflow.add_edge("agent", END)

# Compile the graph
app = workflow.compile()

# --- 5. Run the Graph and Interact ---

print("LangGraph Agent is ready (using local Phi3 model). Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
    # Run the graph with the new human input
    result = app.invoke(
        {"messages": [HumanMessage(content=user_input)]}
    )
    
    # Print the last message from the AI response
    # The messages are stored in a list in the state
    print(f"Bot: {result['messages'][-1].content}")