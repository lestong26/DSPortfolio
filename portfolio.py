import streamlit as st

# Title of the portfolio
st.title("My Portfolio")

# Display an image with a clickable link
st.markdown(
    """
    <a href="https://courseraplus-cmcova.streamlit.app/" target="_blank">
        <img src="pics/coursera_header.png" alt="Dashboard Image" style="width:100%;height:auto;">
    </a>
    """,
    unsafe_allow_html=True
)

# Add a description or other content as needed
st.write("Click the image above to view the Data Science project.")
