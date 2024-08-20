import streamlit as st
from PIL import Image
import base64
from io import BytesIO

# Set page layout to wide
st.set_page_config(layout='wide')

# Function to convert image to base64
def image_to_base64(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Capstone Project
image_path13 = "pics/askwelabscover.png"
image_base64_13 = image_to_base64(image_path13)

# Project 1
image_path1 = "pics/coursera_header.png"
image_base64_1 = image_to_base64(image_path1)

# Project 2
image_path2 = "pics/Intro_Objective.png"
image_base64_2 = image_to_base64(image_path2)

# Project 3
image_path3 = "pics/ml_app.png"
image_base64_3 = image_to_base64(image_path3)

# Project 4
image_path4 = "pics/adobo_front.png"
image_base64_4 = image_to_base64(image_path4)

# Add CSS for the layout
st.markdown(
    """
    <style>
        .project-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            gap: 20px;
            margin-top: 20px;
        }
        .project {
            border: 1px solid #e6e6e6;
            border-radius: 8px;
            padding: 16px;
            background-color: #f9f9f9;
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .project img {
            max-width: 100%;
            border-radius: 8px;
        }
        .project h2 {
            margin-top: 16px;
        }
        .project p {
            text-align: justify;
        }
        .project a {
            margin-top: auto;
            text-decoration: none;
            color: #1a73e8;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Title of the portfolio (centered)
st.markdown(
    """
    <div style="text-align: center;">
        <h1>My Portfolio</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <style>
    .centered-project {{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
        margin: 0 auto 70px auto; /* Centers the container and adds space at the bottom */
        width: 40%; /* Set the width of the container */
    }}
    .centered-project img {{
        max-width: 80%; /* Image will take up 100% of the container's width */
        height: auto;
    }}
    </style>
    <div class="centered-project">
        <div class="project">
            <a href="https://askwelabscapstoneproject.streamlit.app/" target="_blank">
                <img src="data:image/png;base64,{image_base64_13}" alt="Capstone Project Image">
            </a>
            <h2>Askwelabs: AI-Powered Chatbot and Study Path Recommendations</h2>
            <p>Askwelabs is an AI-driven platform offering a Q&A Chatbot that answers common questions about Eskwelabs and analyzes resumes to recommend whether users should join a bootcamp or pursue self-study. It also features a Study Path Recommendation System that creates personalized learning plans based on user preferences in difficulty and focus area, whether Data Analytics or Data Science. Built with ChromaDB, LangChain, and OpenAI’s GPT-3.5 Turbo, Askwelabs delivers tailored educational guidance.</p>
            <a href="https://askwelabscapstoneproject.streamlit.app/" target="_blank">Click here to view</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Second markdown with two projects side by side
st.markdown(
    f"""
    <style>
    .side-by-side-container {{
        display: flex;
        justify-content: space-around;
        align-items: flex-start;
        text-align: center;
    }}
    .side-by-side-container .project {{
        flex: 1;
        margin: 0 40px; /* Adds space between the two projects */
    }}
    .side-by-side-container img {{
        max-width: 80%;
        height: auto;
    }}
    </style>
    <div class="side-by-side-container">
        <div class="project">
            <a href="https://courseraplus-cmcova.streamlit.app/" target="_blank">
                <img src="data:image/png;base64,{image_base64_1}" alt="Project 1 Image">
            </a>
            <h2>Course Recommender App</h2>
            <p>Coursera Plus is a Course Recommender App that makes use of Coursera data to develop a machine learning model that can assist you in deciding the perfect online learning course fit to your needs. The project was built using the OpenAI API key for the LLM Embedding and Retrieval-Augmented Generation (RAG) techniques.</p>
            <a href="https://courseraplus-cmcova.streamlit.app/" target="_blank">Click here to view</a>
        </div>
        <div class="project">
            <a href="https://aitapredictor-cmc.streamlit.app/" target="_blank">
                <img src="data:image/png;base64,{image_base64_2}" alt="Project 2 Image">
            </a>
            <h2>Reddit AITA Predictor</h2>
            <p>This Streamlit app makes use of webscraped subreddit data to develop a machine learning model that can assist you in creating moral judgments in various situations you face in everyday life.</p>
            <a href="https://aitapredictor-cmc.streamlit.app/" target="_blank">Click here to view</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div class="project-container">
        <div class="project">
            <a href="https://mltrafficsafety-cmcova.streamlit.app/" target="_blank">
                <img src="data:image/png;base64,{image_base64_3}" alt="Project 3 Image">
            </a>
            <h2>Self-Accident Detection App</h2>
            <p>Self-Accident Detection App is an app with A Machine Learning Approach to Predict and Prevent Self-Accidents. The goal of this project is to highlight the challenges and propose solutions derived from insights gathered through the application of machine learning techniques.</p>
            <a href="https://mltrafficsafety-cmcova.streamlit.app/" target="_blank">Click here to view</a>
        </div>
        <div class="project">
            <a href="https://eskwelabssprint1-cmcova.streamlit.app/" target="_blank">
                <img src="data:image/png;base64,{image_base64_4}" alt="Project 2 Image">
            </a>
            <h2>Hello, Risk, Goodbye</h2>
            <p>This project is more on exploring and presenting the analysis and insights on the customers of the client: Adobo Advantage Cards.</p>
            <a href="https://eskwelabssprint1-cmcova.streamlit.app/" target="_blank">Click here to view</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
