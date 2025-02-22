import streamlit as st
from utils.display_items import display_items, display_selected_item,display_recomendation_items
from api.endpoints.config import UPCOMING_MOVIES, DISCOVER_MOVIES, DISCOVER_TV, TOP_RATED, TRENDING_ALL
from controllers.get_items import get_items, get_recommendations_items
from utils.btn import navigate_pages_btn

def handle_item_details():
    """Display selected item and recommendations"""
    recommendation_request_end, selected_item_id = display_selected_item()
    if recommendation_request_end and selected_item_id:
        st.title("**Recommendations**")
        st.write("---")
        items_list = get_recommendations_items(recommendation_request_end, 
            id=selected_item_id, 
            pages=1)
        display_recomendation_items(items_list)
        navigate_pages_btn()
    else:
        st.warning("No recommendations available")

def handle_main_content():
    """Display content for the current page"""
    page_to_endpoint = {
        "Trending": TRENDING_ALL,
        "Movies": DISCOVER_MOVIES,
        "Top Rated": TOP_RATED,
        "TV Shows": DISCOVER_TV,
        "Upcoming": UPCOMING_MOVIES,
    }
    
    st.title(f"**{st.session_state.current_page}**")
    
    items_list = get_items(page_to_endpoint[st.session_state.current_page],
        st.session_state.page)
    display_items(items_list)
    navigate_pages_btn()
    
    