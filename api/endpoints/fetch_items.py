import requests
from .config import HEADERS, BASE_URL


def fetch_items(request_end: str ,page=1):
    """Fetch page of popular movies starting from the given page."""
    url = f"{BASE_URL}{request_end}"
    # print(url)
    params = {"page": page, "language": "en-US"}
    response = requests.get(
        url, headers=HEADERS, params=params
    )
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
    elif response.status_code == 204:
        print(f"No content found on page {page}. Response Content: {response.text}")
    else:
        print(f"Failed to fetch page {page}: {response.status_code}")

    return results

def fetch_recommendations_items(request_end: str ,id=1 ,page=1):
    """Fetch movie recommendations based on a given movie ID."""
    url = f"{BASE_URL}{request_end.format(id=id)}"
    print(url)
    
    params = {"page": page, "language": "en-US"}
    response = requests.get(
        url, headers=HEADERS, params=params
    )

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        return results
    else:
        print(f"Failed to fetch recommendations: {response.status_code}")
        return None