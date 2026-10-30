import chromadb
from app.config import settings

# This creates a local folder for your data
client = chromadb.PersistentClient(path="./discovery_db")

def initialize_db():
    # This replaces the complex SQL setup
    client.get_or_create_collection(name="problem_statements")
    print("--- [DATABASE] ChromaDB Local Folder Initialized ---")

def save_discovery(raw_input: str, output: str, embedding: list):
    collection = client.get_or_create_collection(name="problem_statements")
    
    # ChromaDB handles the storage internally
    collection.add(
        documents=[output],
        embeddings=[embedding],
        metadatas=[{"raw_input": raw_input}],
        ids=[str(hash(output))] # Simple unique ID
    )
    print("--- [DATABASE] Discovery Saved Locally ---")