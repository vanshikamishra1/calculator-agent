from langchain.tools import tool
from serpapi import GoogleSearch
import os

@tool
def google_search(query: str) -> str:
    """Perform a Google search using SerpAPI for the input query."""
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_API_KEY"),
        "num": 3
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    output = []

    for res in results.get("organic_results", []):
        title = res.get("title", "")
        link = res.get("link", "")
        output.append(f"{title}\n{link}")

    return "\n\n".join(output) if output else "No results found."
