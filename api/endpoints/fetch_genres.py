import requests
import json
import os
from .config import HEADERS, BASE_URL
from services.const import TV_GENRES, MOVIES_GENRES

def get_genres_list():
    """Fetch genres for both movies and TV shows and combine them into a single dictionary."""
    combined_genres = {}

    # Fetch movie genres
    movie_url = f"{BASE_URL}{MOVIES_GENRES}"
    movie_response = requests.get(movie_url, headers=HEADERS)
    if movie_response.status_code == 200:
        movie_genres = movie_response.json().get("genres", [])
        for genre in movie_genres:
            combined_genres[genre["id"]] = {"name": genre["name"], "type": "movie"}
    else:
        print(f"Failed to fetch movie genres: {movie_response.status_code}")

    # Fetch TV genres
    tv_url = f"{BASE_URL}{TV_GENRES}"
    tv_response = requests.get(tv_url, headers=HEADERS)
    if tv_response.status_code == 200:
        tv_genres = tv_response.json().get("genres", [])
        for genre in tv_genres:
            # If the genre ID already exists, append the type (e.g., "movie,tv")
            if genre["id"] in combined_genres:
                combined_genres[genre["id"]]["type"] += ",tv"
            else:
                combined_genres[genre["id"]] = {"name": genre["name"], "type": "tv"}
    else:
        print(f"Failed to fetch TV genres: {tv_response.status_code}")

    # Save the combined genres to a JSON file
    os.makedirs("src/json", exist_ok=True)
    file_path = "src/json/genres.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(combined_genres, file, indent=4, ensure_ascii=False)

    print(f"Combined genres saved to {file_path}")
    return combined_genres