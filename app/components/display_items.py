import streamlit as st
from st_clickable_images import clickable_images
from services.extract_genre import extract_genre

from services.const import MOVIE_RECOMMENDATION

from controllers.get_items import get_items,get_recommendations_items
from controllers.get_item import get_item

def display_selected_item():
    """Displays the selected movie's details on a separate page."""
    selected_movie = st.session_state.selected_movie

    if selected_movie:
        # Add a "Back" button to return to the main page
        if st.button("<-- Back"):
            st.session_state.selected_movie = None
            st.rerun()
        
        selected_item_id = int(selected_movie.get("id",0))
        item_info = get_item(id=selected_item_id)    
        poster_image, infos, space = st.columns([1.5, 6, 3])
        with poster_image:
            st.image(item_info["poster_url"], use_container_width=True)
        with infos:
            st.subheader(item_info["title"])
            st.write(f"**Release Year:** {item_info.get('releaseYear', 'N/A')}")
            
            ids_genres = item_info.get("genre_ids", [])
            if ids_genres:
                item_info_genres = []
                for id in ids_genres:
                    genre = extract_genre(id)
                    if genre:  # Only append if genre is not None
                        item_info_genres.append(genre)
                        print(genre)
                
                if item_info_genres:  # Only join if there are valid genres
                    st.write(", ".join(item_info_genres))
                else:
                    st.write("No genres available.")
            
            st.write(f"**Overview:** {item_info.get('overview', 'No overview available.')}")
            progress_bar_rating , rating_value,space = st.columns([3,1,6])
            rating = float(item_info.get("vote_average", 0))
            vote_average = float(rating) / 10  # Normalize to 0-1 range
            with rating_value:
                st.caption("")
                st.write(f"**{rating}**")
            with progress_bar_rating :
                st.progress(vote_average,"Rating")

        st.title(f"**Recomendation**")
        st.write("---")
        display_recomendation_items(request_end = MOVIE_RECOMMENDATION,id=selected_item_id,pages=1)       


def display_recomendation_items(request_end:str, id ,pages):
    """Displays a grid of clickable movie images and expands the selected movie's details."""
    items_list = get_recommendations_items(request_end,id=id,pages=pages)

    if not items_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Prepare images and titles for clickable_images
    movie_images = []
    movie_titles = []

    for item in items_list:
        poster_url = item.get("poster_url", "src/empty_poster.jpg")
        caption = f"{item['title']} ({item['release_year']})"
        movie_images.append(poster_url)
        movie_titles.append(caption)

    # Custom CSS for 8-column grid layout with adjusted spacing
    st.markdown(
        """
        <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(8, 1fr); /* 8 columns */
            gap: 20px; /* Increased spacing between items */
            justify-content: center;
        }
        .image-item {
            text-align: center;
        }
        .image-item img {
            width: 100%; /* Fill container width */
            height: auto; /* Maintain aspect ratio */
            border-radius: 5px; /* Rounded corners */
            object-fit: cover; /* Ensure images fill space */
        }
        .image-item p {
            margin: 5px 0; /* Slightly increased spacing for captions */
            font-size: 12px; /* Slightly larger caption text */
            word-wrap: break-word; /* Handle long titles */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Use clickable_images with custom CSS
    clicked_index = clickable_images(
        movie_images,
        titles=movie_titles,  # Add titles as captions
        div_style={"display": "grid", "grid-template-columns": "repeat(8, 1fr)", "gap": "20px"},  # 8-column grid with spacing
        img_style={"width": "100%", "height": "auto", "border-radius": "5px"},  # Customize image size and style
        key=request_end
    )

    # Handle the clicked image
    if clicked_index > -1:
        selected_movie = items_list[clicked_index]
        st.session_state.selected_movie = selected_movie
        st.rerun()  # Rerun the app to display the selected item page

    # Pagination buttons and current page display
    _, previous_col, page_number, next_col, _ = st.columns([4.3, 0.66, 0.5, 1, 4])
    st.write("")

    with previous_col:
        if st.button("<- Prev") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()

    with next_col:
        if st.button("Next ->"):
            st.session_state.page += 1
            st.rerun()

    with page_number:
        st.caption("")
        st.write(f"Page {st.session_state.page}")




def display_items(request_end:str ,page):
    """Displays a grid of clickable movie images and expands the selected movie's details."""
    items_list = get_items(request_end,page)

    if not items_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Prepare images and titles for clickable_images
    movie_images = []
    movie_titles = []

    for item in items_list:
        poster_url = item.get("poster_url", "src/empty_poster.jpg")
        # caption = f"{item['title']} ({item['releaseYear']})"
        movie_images.append(poster_url)
        # movie_titles.append(caption)

    # Custom CSS for 8-column grid layout with adjusted spacing
    st.markdown(
        """
        <style>
        .image-grid {
            display: grid;
            grid-template-columns: repeat(8, 1fr); /* 8 columns */
            gap: 20px; /* Increased spacing between items */
            justify-content: center;
        }
        .image-item {
            text-align: center;
        }
        .image-item img {
            width: 100%; /* Fill container width */
            height: auto; /* Maintain aspect ratio */
            border-radius: 5px; /* Rounded corners */
            object-fit: cover; /* Ensure images fill space */
        }
        .image-item p {
            margin: 5px 0; /* Slightly increased spacing for captions */
            font-size: 12px; /* Slightly larger caption text */
            word-wrap: break-word; /* Handle long titles */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Use clickable_images with custom CSS
    clicked_index = clickable_images(
        movie_images,
        titles=movie_titles,  # Add titles as captions
        div_style={"display": "grid", "grid-template-columns": "repeat(8, 1fr)", "gap": "20px"},  # 8-column grid with spacing
        img_style={"width": "100%", "height": "auto", "border-radius": "5px"},  # Customize image size and style
        key=request_end
    )

    # Handle the clicked image
    if clicked_index > -1:
        selected_movie = items_list[clicked_index]
        st.session_state.selected_movie = selected_movie
        st.rerun()  # Rerun the app to display the selected item page

    # Pagination buttons and current page display
    _, previous_col, page_number, next_col, _ = st.columns([4.3, 0.66, 0.5, 1, 4])
    st.write("")

    with previous_col:
        if st.button("<- Prev") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()

    with next_col:
        if st.button("Next ->"):
            st.session_state.page += 1
            st.rerun()

    with page_number:
        st.caption("")
        st.write(f"Page {st.session_state.page}")
