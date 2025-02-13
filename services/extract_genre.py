import json
import os
from api.endpoints.get_genre_list import get_genres_list

def extract_genre(genre_id):
    """Extracts genre name based on genre_id from the combined genres dictionary."""
    
    # Determine the file path
    file_path = "src/json/genres.json"

    # Check if the JSON file already exists
    if os.path.exists(file_path):
        print(f"📂 Loading combined genres from {file_path}...")
        with open(file_path, "r", encoding="utf-8") as file:
            genres = json.load(file)
    else:
        print(f"🌍 Fetching combined genres from API...")
        genres = get_genres_list()

    # Find the genre name based on genre_id
    # Convert genre_id to string for lookup
    genre_id_str = str(genre_id)

    # Find the genre name based on genre_id
    if genre_id_str in genres:
        return genres[genre_id_str]["name"]
    else:
        print(f"⚠️ Genre ID {genre_id} not found.")
        return None