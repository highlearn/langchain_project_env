from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool

# Example tool
def dummy_search(query: str) -> str:
    return f"Searched for '{query}'"

tools = [
    Tool(name="SearchTool", func=dummy_search, description="A test search tool")
]

llm = ChatOpenAI(temperature=0)

agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

response = agent.run("What is the capital of India?")
print(response)