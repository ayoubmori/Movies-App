from api.endpoints.config import TRENDING_ALL
from utils.display_items import display_backdrop_img_items
from controllers.get_items import get_items
import streamlit as st

def backdrop_slideshow():
    backdrop_area,space=st.columns([5,4])
    with backdrop_area:
        items_list = get_items(TRENDING_ALL, st.session_state.page)
        display_backdrop_img_items(items_list)