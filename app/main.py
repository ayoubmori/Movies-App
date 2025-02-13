import streamlit as st
st.set_page_config(layout="wide")
from app.components.display_items import display_items ,display_selected_item
# Initialize session state for pagination
if "page" not in st.session_state:
    st.session_state.page = 1
if "popular_items" not in st.session_state:
    st.session_state.data_items = []
    
# Initialize session state for selected movie
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
# Main app
from services.const import UPCOMING_MOVIES , DISCOVER_MOVIES , DISCOVER_TV
# Or using Markdown (alternative method)
# st.markdown("# Movies \n---")

# List of available endpoints for selection

if st.session_state.selected_movie:
    # Display the selected movie on its own page
    display_selected_item()
else:
    # Display the grid of movies
    endpoints = [DISCOVER_MOVIES, UPCOMING_MOVIES, DISCOVER_TV]
    # request_end = st.selectbox("Choose the request endpoint", endpoints)
    st.markdown("# DISCOVER MOVIES \n---")
    display_items(st.session_state.page , DISCOVER_MOVIES)
    st.subheader("")
    st.markdown("# UPCOMING MOVIES \n---")
    display_items(st.session_state.page , UPCOMING_MOVIES)
    st.subheader("")
    st.markdown("# DISCOVER TV SHOWS \n---")
    display_items(st.session_state.page , DISCOVER_TV)


