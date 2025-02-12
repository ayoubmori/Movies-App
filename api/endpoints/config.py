import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TMDB_MOVIE_API")
BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

CACHE_EXPIRY = 3600  # Cache duration in seconds

BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"