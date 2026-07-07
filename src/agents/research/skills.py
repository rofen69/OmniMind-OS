"""
Research Skills

Reusable functions for the Research Agent.
"""

import re
import requests


def summarize(topic: str) -> str:
    """
    Search Wikipedia for the given topic and return the top extract.

    Args:
        topic (str): The topic or query to research.

    Returns:
        str: The research summary from Wikipedia.
    """
    # Extract meaningful keywords for Wikipedia search (ignoring common verbs/formats)
    words = [w for w in re.findall(r'[a-zA-Z]+', topic.lower()) if len(w) > 3]
    stop_words = {"research", "find", "search", "what", "evaluate", "score", "judge", "assess", "document", "format", "markdown", "summarize", "summary", "write", "save", "file", "disk", "output", "generate", "documentation", "about", "wikipedia", "info", "information", "please", "could", "would", "that", "this", "with", "from", "into"}
    keywords = [w for w in words if w not in stop_words]
    
    # Use top 3 strongest keywords with fuzzy matching for typos like 'jems' -> 'james'
    query = " ".join(keywords[:3])
    if not query.strip():
        query = "OmniMind"

    url = "https://en.wikipedia.org/w/api.php"
    
    # Search for the closest matching page title
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query + "~",  # ~ enables fuzzy search on Wikipedia
        "format": "json",
        "utf8": 1
    }
    
    headers = {
        "User-Agent": "OmniMindOS/1.0 (Capstone Submission)"
    }
    
    try:
        response = requests.get(url, params=search_params, headers=headers, timeout=10)
        data = response.json()
        search_results = data.get("query", {}).get("search", [])
        
        if not search_results:
            return f"Research results for '{query}': No specific Wikipedia article found."
            
        # Get the title of the top result
        top_title = search_results[0]["title"]
        
        # Now fetch the summary extract for that title
        extract_params = {
            "action": "query",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "titles": top_title,
            "format": "json"
        }
        
        extract_resp = requests.get(url, params=extract_params, headers=headers, timeout=10)
        extract_data = extract_resp.json()
        pages = extract_data.get("query", {}).get("pages", {})
        
        for page_id, page_info in pages.items():
            if "extract" in page_info:
                return f"# Research Summary: {top_title}\n\n{page_info['extract']}"
                
        return f"Research results for '{top_title}': Found article but could not retrieve extract."

    except Exception as e:
        return f"Research failed due to network error: {str(e)}"