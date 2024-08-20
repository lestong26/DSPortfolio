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
    return base64.b64encode(buffered.getvalue()).decode()

# Project details: paths and descriptions
projects = [
    {
        "title": "Askwelabs: AI-Powered Chatbot and Study Path Recommendations",
        "image_path": "pics/askwelabscover.png",
        "description": ("Askwelabs is an AI-driven platform offering a Q&A Chatbot that answers common questions "
                        "about Eskwelabs and analyzes resumes to recommend whether users should join a bootcamp or "
                        "pursue self-study. It also features a Study Path Recommendation System that creates "
                        "personalized learning plans based on user preferences in difficulty and focus area, "
                        "whether Data Analytics or Data Science. Built with ChromaDB, LangChain, and OpenAI’s GPT-3.5 Turbo, "
                        "Askwelabs delivers tailored educational guidance."),
        "link": "https://askwelabscapstoneproject.streamlit.app/"
    },
    {
        "title": "Course Recommender App",
        "image_path": "pics/coursera_header.png",
        "description": ("Coursera Plus is a Course Recommender App that makes use of Coursera data to develop a "
                        "machine learning model that can assist you in deciding the perfect online learning course "
                        "fit to your needs. The project was built using the OpenAI API key for the LLM Embedding "
                        "and Retrieval-Augmented Generation (RAG) techniques."),
        "link": "https://courseraplus-cmcova.streamlit.app/"
    },
    {
        "title": "Reddit AITA Predictor",
        "image_path": "pics/Intro_Objective.png",
        "description": ("This Streamlit app makes use of webscraped subreddit data to develop a machine learning model "
                        "that can assist you in creating moral judgments in various situations you face in everyday life."),
        "link": "https://aitapredictor-cmc.streamlit.app/"
    },
    {
        "title": "Self-Accident Detection App",
        "image_path": "pics/MLDetection.png",
        "description": ("Self-Accident Detection App is an app with A Machine Learning Approach to Predict and Prevent Self-Accidents. "
                        "The goal of this project is to highlight the challenges and propose solutions derived from insights gathered "
                        "through the application of machine learning techniques."),
        "link": "https://mltrafficsafety-cmcova.streamlit.app/"
    },
    {
        "title": "Hello, Risk, Goodbye",
        "image_path": "pics/adobo_front.png",
        "description": ("This project is more on exploring and presenting the analysis and insights on the customers of the client: "
                        "Adobo Advantage Cards."),
        "link": "https://eskwelabssprint1-cmcova.streamlit.app/"
    }
]

# Convert images to base64 and add CSS for layout
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
            max-width: 80%;
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
        <h5>Welcome to my portfolio! Here, you'll find a journey through my projects, starting with customer data analysis for ADOBO Advantage Cards and progressing to the Self-Accident Detection App, a tool to predict and prevent accidents. I explored NLP in the Reddit AITA Predictor, built a course recommender in Coursera Plus, and developed Askwelabs, an AI platform for personalized educational guidance. Explore these projects to see how I've applied advanced techniques to solve real-world challenges.</h5>
    </div>
    """,
    unsafe_allow_html=True
)

# Display projects in sections
for idx, project in enumerate(projects):
    image_base64 = image_to_base64(project['image_path'])
    if idx == 0:
        # First project centered
        st.markdown(
            f"""
            <div class="centered-project" style="text-align:center;">
                <div class="project">
                    <a href="{project['link']}" target="_blank">
                        <img src="data:image/png;base64,{image_base64}" alt="Project Image">
                    </a>
                    <h2>{project['title']}</h2>
                    <p>{project['description']}</p>
                    <a href="{project['link']}" target="_blank">Click here to view</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Subsequent projects side by side
        if idx % 2 == 1:
            st.markdown('<div class="project-container">', unsafe_allow_html=True)
        
        st.markdown(
            f"""
            <div class="project">
                <a href="{project['link']}" target="_blank">
                    <img src="data:image/png;base64,{image_base64}" alt="Project Image">
                </a>
                <h2>{project['title']}</h2>
                <p>{project['description']}</p>
                <a href="{project['link']}" target="_blank">Click here to view</a>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if idx % 2 == 0 or idx == len(projects) - 1:
            st.markdown('</div>', unsafe_allow_html=True)
