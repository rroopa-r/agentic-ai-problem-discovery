from langchain_ollama import ChatOllama

print("Testing connection...")
llm = ChatOllama(model="llama3")
try:
    response = llm.invoke("Say 'Hello World'")
    print("Response from AI:", response.content)
except Exception as e:
    print("Error:", e)