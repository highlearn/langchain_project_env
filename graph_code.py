import operator
from typing import TypedDict, Annotated

# 1. Imports the correct class names
from langgraph.graph import StateGraph, END

# 2. Define the structure of the data that flows through the graph
class GraphState(TypedDict):
    # The 'message' key stores a list of results, merging them using addition (appending)
    message: Annotated[list[str], operator.add]
    name: str # The name we want to greet

# 3. Define the node function
def greet(state: GraphState):
    """
    Takes the name from the state and returns an updated message list.
    """
    name_to_greet = state['name']
    greeting = f"Hello {name_to_greet}!"
    print(greeting)
    
    # Returns an update to the state: specifically updating the 'message' list
    return {"message": [greeting]}

# 4. Initialize the workflow using the StateGraph class
workflow = StateGraph(GraphState)

# Add the function as a node named "greet"
workflow.add_node("greet", greet)

# Set the entry point of the graph
workflow.set_entry_point("greet")

# The graph ends after executing the "greet" node
workflow.add_edge("greet", END)

# Compile the workflow into a runnable app
app = workflow.compile()

# 5. Invoke the graph with initial data
# We provide an initial 'name' and an empty 'message' list
initial_input = {"name": "Manish", "message": []}
result = app.invoke(initial_input)

# The 'result' is the final GraphState dictionary
print(result)