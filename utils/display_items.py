import streamlit as st
from st_clickable_images import clickable_images
from api.endpoints.config import FIND_MOVIE, FIND_TV, TV_IMAGES, MOVIE_IMAGES
from api.endpoints.config import MOVIE_RECOMMENDATION, TV_RECOMMENDATION
from controllers.get_item import get_item, get_item_images

def display_selected_item():
    """Displays the selected movie's details on a separate page."""
    selected_item = st.session_state.selected_item

    if selected_item:
        # Add a "Back" button to return to the main page
        if st.button("<-- Back"):
            st.session_state.selected_item = None
            st.session_state.recommendation_clicked = False  # Reset recommendation flag
            st.rerun()

        selected_item_id = int(selected_item.get("id", 0))

        # Determine the request endpoints based on the selected item type
        request_end_value = selected_item.get("request_end", "").lower()
        if "/tv" in request_end_value:
            find_request_end = FIND_TV
            recommendation_request_end = TV_RECOMMENDATION
            images_request_end = TV_IMAGES
        else:
            find_request_end = FIND_MOVIE
            recommendation_request_end = MOVIE_RECOMMENDATION
            images_request_end = MOVIE_IMAGES

        # Fetch and display item details
        item_info = get_item(request_end=find_request_end, id=selected_item_id)
        item_images = get_item_images(request_end=images_request_end, id=selected_item_id)
        if item_info:
            poster_image, infos, backdrops_imgs = st.columns([1.5, 3, 5])
            with poster_image:
                st.image(item_info["poster_url"], use_container_width=True)
            with infos:
                item_title = item_info["title"]
                st.subheader(item_title)
                release_year = item_info.get('release_date', 'N/A')
                if release_year != 'N/A':
                    release_year = release_year[:4]
                st.write(f"**Release Year:** {release_year}")

                # Display genres
                genres = item_info.get("genres", [])

                if genres:
                    st.write(", ".join(genres))
                else:
                    st.write("No genres available.")

                # Display overview
                overview = item_info.get("overview", None)
                if overview:
                    st.write(f"**Overview:** {overview}")

                # Display rating
                progress_bar_rating, rating_value, space = st.columns([5, 1, 3])
                rating = float(item_info.get("vote_average", 0))
                vote_average = float(rating) / 10  # Normalize to 0-1 range
                with rating_value:
                    st.caption("")
                    st.write(f"**{rating}**")
                with progress_bar_rating:
                    st.progress(vote_average, "Rating")
            with backdrops_imgs:
                display_backdrop_img_items(item_title,release_year,item_images)
        else:
            st.error("Item not found")

        return recommendation_request_end, selected_item_id
    return None, None

def display_recomendation_items(items_list=[]):
    """Displays a grid of clickable movie images and expands the selected movie's details."""

    if not items_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Prepare images and titles for clickable_images
    movie_images = []
    movie_titles = []

    for item in items_list:
        poster_url = item.get("poster_url",item.get("poster_path"))
        caption = f"{item['title']} ({item['release_year']})"
        movie_images.append(poster_url)
        movie_titles.append(caption)

    # Use clickable_images with custom CSS
    clicked_index = clickable_images(
        movie_images,
        titles=movie_titles,
        div_style={"display": "grid", "grid-template-columns": "repeat(8, 1fr)", "gap": "20px"},
        img_style={"width": "100%", "height": "auto", "border-radius": "5px"},
        key=f"{movie_titles[0]}",  # Unique key for recommendations
    )

    # Handle the clicked image
    if clicked_index > -1:
        selected_item = items_list[clicked_index]
        st.session_state.selected_item = selected_item
        st.session_state.recommendation_clicked = True  # Set recommendation flag
        st.rerun()  # Rerun the app to display the selected item page




def display_items(items_list=[]):
    """Displays a grid of clickable movie images and expands the selected movie's details."""

    if not items_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Prepare images and titles for clickable_images
    movie_images = []
    movie_titles = []

    for item in items_list:
        poster_url = item.get("poster_path",item.get('poster_url'))
        if poster_url:
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_url}"
        else :
            continue
        release_date = item.get("release_date",(item.get("first_air_date"),"Unknown"))
        title = item.get("title",(item.get("name"),"Unknown"))
        caption = f"{title} ({release_date[:4]})"
        movie_images.append(poster_url)
        movie_titles.append(caption)

    # Use clickable_images with custom CSS
    clicked_index = clickable_images(
        movie_images,
        titles=movie_titles,
        div_style={"display": "grid", "grid-template-columns": "repeat(8, 1fr)", "gap": "20px"},
        img_style={"width": "100%", "height": "auto", "border-radius": "5px"},

    )
    
    # Handle the clicked image
    if clicked_index > -1:
        selected_item = items_list[clicked_index]
        st.session_state.selected_item = selected_item
        st.session_state.recommendation_clicked = False  # Reset recommendation flag
        st.rerun()  # Rerun the app to display the selected item page
        
        
########################
from streamlit_carousel import carousel
def display_backdrop_img_items(item_title,release_year,items_list=[]):
    """Displays a carousel of clickable movie/TV show backdrop images."""

    if not items_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Prepare items for the carousel
    carousel_items = []
    i = 0
    # Append the formatted item to the carousel items list
    for item_img in items_list:
        carousel_items.append(
            {
                "title": item_title,  # Use the caption as the title
                "text": release_year,  # Use the overview as the text
                "img": item_img,  # Use the backdrop URL as the image
                "key": i,  # Use the item's ID as the key
            }
        )
        i+=1

    carousel(items=carousel_items, fade=True, controls=True,interval=4300,indicators=False)
    




def display_search_result(results):
    if st.button("back"):
        st.session_state.search_results = None
        st.session_state.searching = False
        st.rerun()
    if results :
        if results["movies"]:
            st.subheader("🎥 Movies")
            display_items(results["movies"])

        if results["tv_shows"]:
            st.subheader("📺 TV Shows")
            display_items(results["tv_shows"])

    else:
        st.write("❌ No results found.")