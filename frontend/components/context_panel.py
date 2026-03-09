import streamlit as st


def render_context(context_items):

    if not context_items:
        st.info("No retrieved knowledge available.")
        return

    for idx, item in enumerate(context_items):

        if isinstance(item, dict):

            title = item.get("title", f"Source {idx+1}")
            content = item.get("content", "")

        else:

            title = f"Source {idx+1}"
            content = str(item)

        with st.expander(title):
            st.write(content)