import streamlit as st


def render_solution(result):

    if not result:
        st.warning("No solution generated.")
        return

    solution = result.get("solution")
    explanation = result.get("explanation")
    steps = result.get("steps", [])

    st.markdown("## 🧮 Step-by-Step Solution")

    # Show steps if structured steps exist
    if steps:

        for i, step in enumerate(steps, 1):

            st.markdown(f"### Step {i}")
            st.write(step)

    # Show explanation only once
    if explanation:

        st.markdown("### Explanation")
        st.write(explanation)

    # Final Answer
    if solution:

        st.success(f"Final Answer: {solution}")