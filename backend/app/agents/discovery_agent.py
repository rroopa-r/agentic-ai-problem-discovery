import sys
import os

# Adds the 'backend' directory to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import operator
from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from app.tools.web_research import search_online_research


class GraphState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]
    raw_input: str


def research_node(state: GraphState):
    topic = state["raw_input"]
    print(f"--- [AGENT] Searching online for: {topic} ---")
    search_results = search_online_research(topic)
    return {"messages": [search_results]}

def discovery_node(state: GraphState):
    print("--- [AGENT] STARTING ANALYSIS ---")
    context = state["messages"][-1]
    prompt = f"Using this research: {context}, summarize the main problem for {state['raw_input']} in 3 sentences."
    llm = ChatOllama(model="tinyllama", temperature=0)
    response = llm.invoke(prompt)
    return {"messages": [response.content]}

# --- 1. Initialize the Local Brain ---
# Using tinyllama as you specified, but llama3 is recommended for better "Problem Discovery"
llm = ChatOllama(model="tinyllama", temperature=0)


builder = StateGraph(GraphState)

# This will now work because research_node is defined above!
builder.add_node("researcher", research_node)
builder.add_node("analyzer", discovery_node)

builder.set_entry_point("researcher")
builder.add_edge("researcher", "analyzer")
builder.add_edge("analyzer", END)

graph = builder.compile()