from api.endpoints.config import BASE_IMAGE_URL
import streamlit as st

@st.cache_resource()
def extract_item_info(results):
    if not results:
        return None

    movie_details = {
        "id": results.get("id", "Unknown"),
        "title": results.get("original_title", "No Title"),
        "overview": results.get("overview", "No overview available."),
        "original_language": results.get("original_language", "Unknown"),
        "vote_average": results.get("vote_average", 0.0),
        "vote_count": results.get("vote_count", 0),
        "release_date": results.get("release_date", "Unknown"),
        "release_year": results.get("release_date", "Unknown")[:4] if results.get("release_date") else "Unknown",
        "tagline": results.get("tagline", ""),
        "homepage": results.get("homepage", ""),
        "runtime": results.get("runtime", 0),
        "status": results.get("status", "Unknown"),
        "budget": results.get("budget", 0),
        "revenue": results.get("revenue", 0),
        "popularity": results.get("popularity", 0.0),
        "video": results.get("video", False),
        "adult": results.get("adult", False),
        "imdb_id": results.get("imdb_id", ""),
    }

    # Genre Names
    genres = results.get("genres", [])
    movie_details["genres"] = [genre["name"] for genre in genres] if genres else ["Unknown"]

    # # Collection Info
    # collection = results.get("belongs_to_collection", {})
    # movie_details["collection_name"] = collection.get("name", "No Collection")
    # movie_details["collection_poster"] = f"{BASE_IMAGE_URL}{collection.get('poster_path', '')}" if collection.get("poster_path") else None
    # movie_details["collection_backdrop"] = f"{BASE_IMAGE_URL}{collection.get('backdrop_path', '')}" if collection.get("backdrop_path") else None

    # Image Paths
    poster_path = results.get("poster_path", "")
    backdrop_path = results.get("backdrop_path", "")
    movie_details["poster_url"] = f"{BASE_IMAGE_URL}{poster_path}" if poster_path else None
    movie_details["backdrop_url"] = f"{BASE_IMAGE_URL}{backdrop_path}" if backdrop_path else None

    # # Production Companies
    # production_companies = results.get("production_companies", [])
    # movie_details["production_companies"] = [company["name"] for company in production_companies] if production_companies else ["Unknown"]

    # # Production Countries
    # production_countries = results.get("production_countries", [])
    # movie_details["production_countries"] = [country["name"] for country in production_countries] if production_countries else ["Unknown"]

    # Spoken Languages
    spoken_languages = results.get("spoken_languages", [])
    movie_details["spoken_languages"] = [lang["english_name"] for lang in spoken_languages] if spoken_languages else ["Unknown"]

    return movie_details