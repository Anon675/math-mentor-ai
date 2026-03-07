import streamlit as st

def show_context(context_list):

    st.markdown("### Retrieved Knowledge")

    if not context_list:
        st.info("No context retrieved")

    for i, ctx in enumerate(context_list):
        with st.expander(f"Source {i+1}"):
            st.write(ctx)