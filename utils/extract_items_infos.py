from api.endpoints.config import BASE_IMAGE_URL
import streamlit as st

@st.cache_resource()
def extract_items_list(results,request_end):
    """Extracts relevant movie details from the API response."""
    if not results:
        return None

    items_list = []

    for item in results:
        item_details = {
            "id": item.get("id", "Unknown id"),
            "title": item.get("original_title", item.get("original_name", "No Title")),
            # "overview": item.get("overview", "Unknown Overview"),
            "original_language": item.get("original_language", "Unknown"),
            # "vote_average": item.get("vote_average", 0.0),
            "release_date": item.get("release_date", item.get("first_air_date", "Unknown")),
            "request_end":request_end,
            "backdrop_path":item.get("backdrop_path",None)
        }

        # Extract release year
        item_details["release_year"] = (
            item_details["release_date"][:4] if item_details["release_date"] else "Unknown"
        )


        # Extract poster and backdrop images
        poster_path = item.get("poster_path", "")
        # backdrop_path = item.get("backdrop_path", "")

        item_details["poster_url"] = f"{BASE_IMAGE_URL}{poster_path}" if poster_path else None
        # item_details["backdrop_url"] = f"{BASE_IMAGE_URL}{backdrop_path}" if backdrop_path else None
        item_details["image_caption"] = f"{item_details['title']} ({item_details['release_year']})" if item_details["poster_url"] else "No Caption"

        items_list.append(item_details)

    return items_list[:24]  # Return only the first 24 items
