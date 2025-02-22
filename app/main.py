import streamlit as st
from utils.handle_content import handle_item_details, handle_main_content
from app.components.navbar import main_navbar
from app.components.search_box import search_box

# Page Config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# Initialize session state (first run only)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Trending"
if "page" not in st.session_state:
    st.session_state.page = 1
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None
if "searching" not in st.session_state:
    st.session_state.searching = False

# Create navigation bar (preserve state between runs)
current_page = main_navbar()

# Update current page if changed
if current_page != st.session_state.current_page:
    st.session_state.current_page = current_page
    st.session_state.selected_item = None  # Reset selection on page change
    st.rerun()

# search box
search_box()


from api.endpoints.config import TRENDING_ALL
from utils.display_items import display_backdrop_img_items
from controllers.get_items import get_items

# backdrop_area,space=st.columns([4,8])
# with backdrop_area:
#     items_list = get_items(TRENDING_ALL, st.session_state.page)
#     display_backdrop_img_items(items_list)

items_list = get_items(TRENDING_ALL, st.session_state.page)
display_backdrop_img_items(items_list)

# Handle page content
if st.session_state.selected_item:
    handle_item_details()
else:
    handle_main_content()
