from api.endpoints.get_items import get_items
from datetime import date
from pprint import pprint
from api.endpoints.config import BASE_IMAGE_URL
import streamlit as st

@st.cache_resource()
def extract_items_list(page, request_end):
    print("in popular_items list fun ")

    itms_list = []  # Initialize the list
    results = get_items(page, request_end)
    
    if results :
        st.session_state.data_items = results
        # pprint(results)
        for item in results:  # Ensure "results" key exists
            popular_item_details = {}
            # General Infos
            
            popular_item_details["id"] = item.get("id", "Unknown id")
            popular_item_details["title"] = item.get("original_title",item.get("original_name", "No Title"))
            popular_item_details["overview"] = item.get("overview", "Unknown Overview")
            popular_item_details["original_language"] = item.get("original_language", "Unknown original_language")
            popular_item_details["vote_average"] = item.get("vote_average", "Unknown vote_average")
            
            # genres
            popular_item_details["genre_ids"] = item.get("genre_ids", "Unknown genre_ids")
            
            # Format date safely
            popular_item_details["releaseDate"] = item.get("release_date", item.get("first_air_date",{}))
            popular_item_details["releaseYear"] = popular_item_details["releaseDate"][:4] if popular_item_details["releaseDate"] else "Unknown"
            
            # poster image 
            poster_path = item.get("poster_path", "")
            backdrop_path = item.get("backdrop_path", "")
            
            popular_item_details["image_url"] = f"{BASE_IMAGE_URL}{poster_path}" if poster_path else "No Image Available"
            popular_item_details["backdrop_url"] = f"{BASE_IMAGE_URL}{backdrop_path}" if backdrop_path else "No Image Available"
            
            if popular_item_details["image_url"]:
                popular_item_details["image_caption"] = f"{popular_item_details["title"]} ({popular_item_details["releaseYear"]})"
            else:
                popular_item_details["image_caption"] = "No Caption"

            itms_list.append(popular_item_details)
        return itms_list[:24]
    return None
