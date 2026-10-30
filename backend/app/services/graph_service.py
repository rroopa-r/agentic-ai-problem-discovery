from langgraph.graph import StateGraph, END
from app.schemas.state import DiscoveryState
from app.agents.discovery_agent import discovery_node
from app.agents.refinement_agent import refinement_node

def run_discovery_pipeline(user_input: str):
    # Initialize the Graph
    workflow = StateGraph(DiscoveryState)

    # Add Nodes
    workflow.add_node("discoverer", discovery_node)
    workflow.add_node("refiner", refinement_node)

    # Define Flow
    workflow.set_entry_point("discoverer")
    workflow.add_edge("discoverer", "refiner")
    workflow.add_edge("refiner", END)

    # Compile and Run
    app = workflow.compile()
    return app.invoke({"raw_input": user_input})