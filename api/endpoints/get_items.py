import requests

# from tenacity import retry, stop_after_attempt, wait_exponential
from .config import HEADERS, BASE_URL
from pprint import pprint
from services.const import DISCOVER_MOVIES

def get_items(page,request_end= DISCOVER_MOVIES ):
    """Fetch two pages of popular movies starting from the given page."""
    combined_results = []
    for p in [page, page + 1]:  # Fetch two consecutive pages
        url = f"{BASE_URL}{request_end}"
        print(url)
        params = {"page": p, "language": "en-US"}
        response = requests.get(
            url, headers=HEADERS, params=params
        )
        if response.status_code == 200:
            data = response.json()
            combined_results.extend(data.get("results", []))
        elif response.status_code == 204:
            print(f"⚠️ No content found on page {p}. Response Content: {response.text}")
        else:
            print(f"⚠️ Failed to fetch page {p}: {response.status_code}")

    return combined_results

