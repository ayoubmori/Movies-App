import streamlit as st
from streamlit_navigation_bar import st_navbar

def main_navbar():
    # Define navigation pages
    PAGES = ["Home","Trending","Movies","Top Rated", "TV Shows", "Upcoming"]

    # Navigation bar options
    nav_options = {
        "show_menu": True,
        "show_sidebar": False,
        "hide_nav": False,
        "fix_shadow": False,
        "use_padding": True,
    }

    # Custom styles for navigation bar
    NAV_STYLES = {
        "nav": {
            "background-color": "rgb(47, 131, 248)",
        },
        "div": {
            "max-width": "40rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "#F6F1F1",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgba(0, 0, 0, 0.2)",
            "font-weight": "bold",
            "color": "#F6F1F1",
        },
        "hover": {
            "background-color": "rgba(255, 255, 255, 0.35)",
        },
    }
    
    
    current_page = st_navbar(
    PAGES,
    styles=NAV_STYLES,
    selected=st.session_state.current_page,
    options=nav_options,
    key="main_navbar",
    )
    return current_page