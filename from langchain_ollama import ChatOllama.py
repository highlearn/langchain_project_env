from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:latest")
response = llm.invoke("Explain LangChain in simple terms.")
print(response)