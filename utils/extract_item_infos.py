from api.endpoints.config import BASE_IMAGE_URL
import streamlit as st

@st.cache_resource()
def extract_item_info(results):
    if not results:
        return None

    item_details = {
        "id": results.get("id", "Unknown"),
        "title": results.get("original_title", results.get("name","No Title")),
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
        "number_of_episodes" : results.get("number_of_episodes",None)
    }

    # Genre Names
    genres = results.get("genres", [])
    item_details["genres"] = [genre["name"] for genre in genres] if genres else ["Unknown"]

    # Image Paths
    poster_path = results.get("poster_path", "")
    backdrop_path = results.get("backdrop_path", "")
    item_details["poster_url"] = f"{BASE_IMAGE_URL}{poster_path}" if poster_path else None
    item_details["backdrop_url"] = f"{BASE_IMAGE_URL}{backdrop_path}" if backdrop_path else None
    
    # Spoken Languages
    spoken_languages = results.get("spoken_languages", [])
    item_details["spoken_languages"] = [lang["english_name"] for lang in spoken_languages] if spoken_languages else ["Unknown"]

    return item_details


def extract_item_images(results):
    images_path_list = []
    
    for result in results:
        image_path = result.get("file_path",None)
        if image_path:
            image_path = f"{BASE_IMAGE_URL}{image_path}"
            images_path_list.append(image_path)
    
    return images_path_list