from langchain_community.tools import DuckDuckGoSearchResults
from duckduckgo_search import DDGS

def search_online_research(topic): # Renamed to match your agent import
    try:
        print(f"--- [TOOL] Fetching live data for: {topic} ---")
        with DDGS() as ddgs:
            # We fetch the 'body' (text) of the top 3 search results
            results = [r['body'] for r in ddgs.text(topic, max_results=3)]
            
            if not results:
                return "No specific web results found."
                
            return " ".join(results)
    except Exception as e:
        # This helps you see if the library is actually installed
        return f"Search error: Could not import ddgs python package. Please install it with `pip install -U duckduckgo-search`. Original error: {e}"