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
        
def handle_home_content():
    sections = [
        ("Trending", TRENDING_ALL),
        ("Movies", DISCOVER_MOVIES),
        ("TV Shows", DISCOVER_TV),
    ]
    
    for title, category in sections:
        container = st.empty()  # Placeholder for skeletons
        display_skeleton_grid(rows=2, cols=8, container=container)
        items = get_items(category, st.session_state.page)
        if items:
            st.header(title)
            container.empty()  # Remove skeletons
            display_items(items[:16])

def handle_main_content():
    """Display content for the current page."""
    page_to_endpoint = {
        "Trending": TRENDING_ALL,
        "Movies": DISCOVER_MOVIES,
        "Top Rated": TOP_RATED,
        "TV Shows": DISCOVER_TV,
        "Upcoming": UPCOMING_MOVIES,
    }
    
    if st.session_state.current_page == "Home":
        handle_home_content()
    else:
        st.title(f"**{st.session_state.current_page}**")
        items_list = get_items(page_to_endpoint[st.session_state.current_page],
            st.session_state.page)
        display_items(items_list)
        navigate_pages_btn()
    
    
    
    
    

# Some code
from streamlit.proto.Skeleton_pb2 import Skeleton as SkeletonProto


def display_skeleton_grid(rows, cols, container):
    with container:
        for _ in range(rows):
            for col in st.columns(cols):
                with col:
                    skeleton_proto = SkeletonProto()
                    st._main._enqueue("skeleton", skeleton_proto)

# # Function to create a grid of images
# def display_image_grid(image_urls, cols):
#     """Display a grid of images."""
#     for i in range(0, len(image_urls), cols):  # Iterate in steps of `cols`
#         row_images = image_urls[i:i + cols]  # Get images for the current row
#         columns = st.columns(cols)  # Create a row of columns
#         for idx, col in enumerate(columns):
#             if idx < len(row_images):  # Check if there's an image for this column
#                 with col:
#                     st.image(row_images[idx], use_column_width=True)  # Display image
                    