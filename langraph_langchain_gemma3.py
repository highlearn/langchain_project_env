from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables if needed
load_dotenv()

# --- Define structured response model ---
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# --- Initialize Ollama LLM (local Gemma3) ---
llm = ChatOllama(model="gemma3", temperature=0.3)

# --- Create parser for structured output ---
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# --- Define the agent prompt template ---
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that generates concise research summaries.
            Use tools when needed. Return results in the required structured format.
            {format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# --- Load tools ---
tools = [search_tool, wiki_tool, save_tool]

# --- Create the tool-calling agent ---
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

# --- Execute the agent ---
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("Capital of India? ")

raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("⚠️ Error parsing response:", e)
    print("Raw Response:", raw_response)