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

### Endpoints
# DISCOVER
DISCOVER_MOVIES = "/discover/movie"
DISCOVER_TV = "/discover/tv"
UPCOMING_MOVIES = "/movie/popular"
TOP_RATED = "/movie/top_rated"
TRENDING_ALL = "/trending/all/week"

## Genres
MOVIES_GENRES = "/genre/movie/list"
TV_GENRES = "/genre/tv/list"

# RECOMMENDATION
MOVIE_RECOMMENDATION = "/movie/{id}/recommendations"
TV_RECOMMENDATION = "/tv/{id}/recommendations"

#find
FIND_MOVIE = "/movie/{id}"
FIND_TV = "/tv/{id}"


#search
SEARCH_KEYWORD = "/search/keyword"
SEARCH_MULTI = "/search/multi"