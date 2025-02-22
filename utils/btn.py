import streamlit as st
import random


def navigate_pages_btn():
    # Pagination buttons and current page display
    _, previous_col, page_number, next_col, _ = st.columns([4.3, 1, 0.5, 1, 4])
    st.write("")

    with previous_col:
        if st.button("<- Prev",key=str(random.uniform(1.0, 100.0))) and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()

    with next_col:
        if st.button("Next ->",key=str(random.uniform(1.0, 100.0))):
            st.session_state.page += 1
            st.rerun()

    with page_number:
        st.caption("")
        st.write(f"{st.session_state.page}")