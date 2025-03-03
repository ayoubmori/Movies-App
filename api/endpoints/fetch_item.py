import requests
from .config import HEADERS, BASE_URL


def fetch_item(request_end: str,id=1 ):
    """Fetch page of popular movies starting from the given page."""
    url = f"{BASE_URL}{request_end.format(id=id)}"

    params = {"language": "en-US"}
    response = requests.get(
        url, headers=HEADERS, params=params
    )
    if response.status_code == 200:
        results = response.json()
        return results
    else:
        print(f"Failed to fetch item {id}: {response.status_code}")

    return None

def fetch_item_images(request_end: str,id=1):
    """Fetch page of popular movies starting from the given page."""
    url = f"{BASE_URL}{request_end.format(id=id)}"

    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        results = data.get("backdrops")
        return results
    else:
        print(f"Failed to fetch item {id}: {response.status_code}")
    return None