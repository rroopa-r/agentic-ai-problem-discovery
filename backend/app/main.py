import os
from app.agents.discovery_agent import graph

def run_discovery_pipeline():
    print("---------------------------------------")
    print("PROJECT: Agentic Problem Discovery")
    print("STATUS: Initializing...")
    print("---------------------------------------")

    # 1. Prepare the Input
    # This matches the 'messages' key expected by your GraphState
    inputs = {
        "messages": ["Analyze the core challenges of urban waste management in smart cities."]
    }

    print("STAGING: Starting Agentic Discovery Pipeline...")

    try:
        # 2. Run the Compiled Graph
        # This will call discovery_node inside discovery_agent.py
        result = graph.invoke(inputs)

        print("\n--- FINAL PIPELINE OUTPUT ---")
        # Print the last message in the sequence (the AI's answer)
        print(result["messages"][-1])
        print("---------------------------------------")

    except Exception as e:
        print(f"ERROR: Pipeline failed. Details: {e}")

if __name__ == "__main__":
    # Ensure the terminal knows where to find your files
    run_discovery_pipeline()

import uvicorn
from app.database.vector_store import initialize_db


# --- ENABLE CORS ---
# This allows your React frontend (usually on port 3000 or 5173) to talk to this API
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.agents.discovery_agent import graph

app = FastAPI()

# 1. ALLOW THE FRONTEND TO TALK TO US
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DiscoveryRequest(BaseModel):
    topic: str

@app.post("/discovery")
async def run_discovery(request: DiscoveryRequest):
    print(f"--- [PIPELINE] Starting Discovery for: {request.topic} ---")
    
    # 2. RUN THE LANGGRAPH
    inputs = {"raw_input": request.topic, "messages": []}
    result = graph.invoke(inputs)
    
    # 3. RETURN THE FINAL RESULT
    return {"analysis": result["messages"][-1]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

