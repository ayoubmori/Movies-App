import requests
from .config import HEADERS, BASE_URL
import streamlit as st


@st.cache_data(ttl=60)
def search_multi(query,request_end="/search/multi", page=1):
    
    url = f"{BASE_URL}{request_end}"
    print(url)
    params = {"language": "en-US",
              'query': query,}
    response = requests.get(
        url, headers=HEADERS, params=params
    )
    if response.status_code == 200:
        results = response.json()['results']
        return results
    else:
        print(f"Failed to fetch item {id}: {response.status_code}")