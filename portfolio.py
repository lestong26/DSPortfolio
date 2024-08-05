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

# Add a description or other content as needed
st.write("Click the image above to view the Data Science project.")

st.write("Click the image above to view the Data Science project.")
