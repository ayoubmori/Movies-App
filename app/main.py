import streamlit as st
from utils.handle_content import handle_item_details, handle_main_content
from app.components.navbar import main_navbar
from app.components.search_box import search_box
from utils.display_items import display_search_result

# Page Config
st.set_page_config(page_title="Movie app",layout="wide", initial_sidebar_state="collapsed")


# Initialize session state (first run only)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"
    
if "page" not in st.session_state:
    st.session_state.page = 1
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None
if "search_results" not in st.session_state:
    st.session_state.search_results = None
if "searching" not in st.session_state:
    st.session_state.searching = False

# Create navigation bar (preserve state between runs)
current_page = main_navbar()

# Update current page if changed
if current_page != st.session_state.current_page:
    st.session_state.current_page = current_page
    st.session_state.page = 1
    st.session_state.selected_item = None  # Reset selection on page change
    st.rerun()
   
# search box
search_box()



# Handle page content
if st.session_state.selected_item:
    handle_item_details()
elif st.session_state.search_results is not None :
    display_search_result(st.session_state.search_results)
else:
    handle_main_content()
