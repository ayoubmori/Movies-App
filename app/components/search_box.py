import streamlit as st
from controllers.search import categorize_results
from utils.display_items import display_items

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
# icon("search")


def search_box():
    local_css("src/css/style.css")
    # Search input
    right_scpace, search_bar,search_icon,left_space = st.columns([5.5,5,1,5])
    with search_bar:
        query = st.text_input(" ",placeholder="search for movies, TV shows, or people:")
    with search_icon:
        button_clicked = st.button("",icon=":material/search:",key="search_btn")
    # Perform search only if query is at least 2 characters long
    if button_clicked or query :
        if len(query) > 1:
            results = categorize_results(query)
            if results :
                if results["movies"]:
                    st.subheader("🎥 Movies")
                    display_items(results["movies"])

                if results["tv_shows"]:
                    st.subheader("📺 TV Shows")
                    display_items(results["tv_shows"])
            
                # if results["people"]:
                #     st.subheader("🧑 People")
                #     items_list = display_search_results(results["people"])
                #     for person in items_list:
                #         st.write(f"🎭 **{person['name']}** (ID: {person['id']})")

            else:
                st.write("❌ No results found.")
        else:
            st.write("ℹ️ Please enter at least 2 characters to search.")
        
