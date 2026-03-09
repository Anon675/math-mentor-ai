import streamlit as st


def render_agent_trace(trace):

    if not trace:
        st.info("No agent execution trace available.")
        return

    for step in trace:

        agent = step.get("agent", "Agent")
        action = step.get("action", "")
        output = step.get("output", "")

        with st.expander(agent):

            if action:
                st.markdown(f"**Action:** {action}")

            if output:
                st.write(output)