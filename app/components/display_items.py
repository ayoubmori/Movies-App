import streamlit as st
from services.extract_items_infos import extract_items_list

# Function to display the movies
st.fragment
def display_items(page=1 , request_end=None):
    # Get data for two pages (current page and next page)
    popular_movies_list = extract_items_list((page - 1) * 2 + 1,request_end)

    if not popular_movies_list:  # Check if API response is empty
        st.error("⚠️ Failed to fetch movie data.")
        return

    # Define the number of columns per row (e.g., 4 columns)
    num_columns = 8
    columns = st.columns(num_columns)

    # Loop through the movies and display them in the grid
    for index, item in enumerate(popular_movies_list):
        with columns[index % num_columns]:
            if item.get("image_url"):
                st.image(item["image_url"], caption=item["image_caption"], use_container_width=True)
            else:
                st.image("src/empty_poster.jpg", caption=f"{item['title']} ({item['releaseYear']})", use_container_width=True)

    # Pagination buttons and current page display
    _, previous_col, page_number, next_col, _ = st.columns([4.3, 0.66, 0.5, 1, 4])
    st.write("")
    # Previous button logic
    with previous_col:
        if st.button("<- Prev") and st.session_state.page > 1:
            st.session_state.page -= 1  # Decrease page number by 1
            st.rerun()  # Rerun to update the display

    # Next button logic
    with next_col:
        if st.button("Next ->"):
            st.session_state.page += 1  # Increase page number by 1
            st.rerun()  # Rerun to update the display

    # Display current page number
    with page_number:
        st.caption("")
        st.write(f"Page {st.session_state.page}")