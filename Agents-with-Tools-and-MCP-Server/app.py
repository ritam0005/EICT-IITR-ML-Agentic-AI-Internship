import streamlit as st
from crew.crew_setup import run_crew

st.set_page_config(
    page_title="Multi-Agent Analytics Assistant",
    page_icon="🤖",
    layout="wide",
)

st.title("🤖 Multi-Agent Analytics Assistant")

st.write(
    """
Ask business analytics or machine learning questions.
The Supervisor Agent will delegate the task to the appropriate agent.
"""
)

user_query = st.text_area(
    "Enter your question:",
    height=150,
)

if st.button("Analyze"):

    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Agents are working..."):

            try:
                result = run_crew(user_query)

                st.success("Analysis Completed")

                st.markdown(result)

            except Exception as e:
                st.error(str(e))