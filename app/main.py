import streamlit as st
from services.const import UPCOMING_MOVIES, DISCOVER_MOVIES, DISCOVER_TV, TOP_RATED, TRENDING_ALL
from app.components.display_items import display_items, display_selected_item
from streamlit_navigation_bar import st_navbar

# Set page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Define navigation bar pages and styles
pages = ["Trending","Movies","Top Rated", "TV Shows", "Upcoming"]
styles = {
    "nav": {
        "background-color": "#09122C",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

# Create the navigation bar
page = st_navbar(pages, styles=styles)

# Initialize session state for pagination
if "page" not in st.session_state:
    st.session_state.page = 1
if "data_items" not in st.session_state:
    st.session_state.data_items = []

# Initialize session state for selected movie
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# Function to reset selected movie
def return_selected_item_none():
    if "selected_movie" in st.session_state and st.session_state.selected_movie is not None:
        st.session_state.selected_movie = None
        st.rerun()

# Main app logic
if "selected_movie" in st.session_state and st.session_state.selected_movie:
    # Display the selected movie details
    display_selected_item()
else:
    # Handle navigation based on the selected page
    if page == "Trending":
        return_selected_item_none()
        st.title(f"**{page}**")
        display_items(TRENDING_ALL,st.session_state.page)
    elif page == "Movies":
        return_selected_item_none()
        st.title(f"**{page}**")
        display_items(DISCOVER_MOVIES,st.session_state.page)
    elif page == "Top Rated":
        return_selected_item_none()
        st.title(f"**{page}**")
        display_items(TOP_RATED,st.session_state.page)

    elif page == "TV Shows":
        return_selected_item_none()
        st.title(f"**{page}**")
        display_items(DISCOVER_TV,st.session_state.page)

    elif page == "Upcoming":
        return_selected_item_none()
        st.title(f"**{page}**")
        display_items(UPCOMING_MOVIES,st.session_state.page)