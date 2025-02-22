from api.endpoints.search import search_multi

def categorize_results(query):
    """
    Fetches TMDB search results and categorizes them into Movies, TV Shows, and People.

    Args:
        query (str): Search term.
        api_key (str): Your TMDB API key.

    Returns:
        dict: Categorized results (movies, tv_shows, people).
    """
    results = search_multi(query)

    categorized = {
        "movies": [item for item in results if item["media_type"] == "movie"],
        "tv_shows": [item for item in results if item["media_type"] == "tv"],
        "people": [item for item in results if item["media_type"] == "person"]
    }
    
    return categorized