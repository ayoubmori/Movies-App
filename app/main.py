import streamlit as st
st.set_page_config(layout="wide")
from app.components.display_items import display_items
# Initialize session state for pagination
if "page" not in st.session_state:
    st.session_state.page = 1
if "popular_items" not in st.session_state:
    st.session_state.data_items = []

# Main app
from services.const import UPCOMING_MOVIES , DISCOVER_MOVIES , DISCOVER_TV
# Or using Markdown (alternative method)
st.markdown("# Popular Movies \n---")

# List of available endpoints for selection
endpoints = [DISCOVER_MOVIES, UPCOMING_MOVIES, DISCOVER_TV]

# Select endpoint using Streamlit's selectbox
request_end = st.selectbox("Choose the request endpoint", endpoints)
# Display the movies
display_items(st.session_state.page , request_end)

