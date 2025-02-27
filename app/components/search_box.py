import streamlit as st
from controllers.search import categorize_results
from app.components.utils import local_css
from st_keyup import st_keyup
import time


def search_box():
    local_css("src/css/style.css")
    # Search input with button layout
    left_space, search_bar, search_icon, right_space = st.columns([5.5, 5, 1, 5.5])
    
    with search_bar:
        # Real-time input with 800ms debounce
        query = st_keyup(
            " ",
            placeholder="search for movies, TV shows, or people:",
            debounce=800,  # Increased debounce time
            key="search_input"
        )
    
    with search_icon:
        button_clicked = st.button("", icon=":material/search:", key="search_btn")

    # Initialize session state tracking
    if 'search_initialized' not in st.session_state:
        st.session_state.search_initialized = False
        st.session_state.last_search_time = 0
        st.session_state.last_valid_query = ""

    current_time = time.time()
    min_delay = 0.5  # 1.5 seconds between API calls

    # Check if user has initiated a search action
    if query or button_clicked:
        st.session_state.search_initialized = True

    # Handle valid search conditions
    if st.session_state.search_initialized:
        if len(query) > 1:
            # Check if enough time has passed since last search
            time_since_last = current_time - st.session_state.last_search_time
            time_remaining = max(min_delay - time_since_last, 0)
            
            if (button_clicked or query != st.session_state.last_valid_query) and time_since_last >= min_delay:
                with st.spinner("🔍 Searching..."):
                    results = categorize_results(query)
                    st.session_state.search_results = results
                    st.session_state.last_search_time = current_time
                    st.session_state.last_valid_query = query
        elif len(query) <= 1 and len(query) > 0 and (button_clicked or query != st.session_state.last_valid_query):
            st.warning("ℹ️ Please enter at least 2 characters to search.")
            st.session_state.search_results = None

    # Clear results when query is empty
    if not query:
        st.session_state.search_results = None
        st.session_state.search_initialized = False