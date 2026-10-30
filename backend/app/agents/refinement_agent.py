from langchain_openai import ChatOpenAI
from app.config import settings

# Initialize OpenAI GPT-4o
openai = ChatOpenAI(
    model="gpt-4o",
    api_key=settings.OPENAI_API_KEY,
    temperature=0.7
)

def refinement_node(state):
    """OpenAI critiques and refines the problem found by Claude."""
    last_problem = state["discovered_problems"][-1]
    prompt = f"Critique and improve this problem statement for a professional pitch: {last_problem}"
    response = openai.invoke(prompt)
    return {"refined_statement": response.content, "critiques": [response.content]}