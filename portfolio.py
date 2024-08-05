import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Function to convert image to base64
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Title of the portfolio
st.title("My Portfolio")

# Image path
image_path = "pics/coursera_header.png"
image_base64 = image_to_base64(image_path)

# Display an image with a clickable link
st.markdown(
    f"""
    <a href="https://courseraplus-cmcova.streamlit.app/" target="_blank">
        <img src="data:image/png;base64,{image_base64}" alt="Dashboard Image" style="width:100%;height:auto;">
    </a>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align: center;">
        <p>Click the image above to view the Data Science project.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("Coursera Plus is a Course Recommender App that makes use of Coursera data to develop a machine learning model that can assist you in deciding the perfect online learning course fit to your needs. We implemented a system where user queries are embedded to retrieve the top n most similar results from our knowledge base. Users can apply filters to refine the suggestions based on their preferences. The selected courses are then summarized using ChatGPT, highlighting how they can benefit the user according to their initial query. The project was built using the OpenAI API key and Retrieval-Augmented Generation (RAG) techniques") 
