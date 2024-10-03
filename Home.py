import streamlit as st
import base64
from streamlit_extras.switch_page_button import switch_page

# Set page configuration to wide
st.set_page_config(page_title="Dietary Options", layout="wide")

# Hide sidebar while keeping it closed
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;} /* Hide the main menu */
    footer {visibility: hidden;}    /* Hide the footer */
    header {visibility: hidden;}    /* Hide the header */
    [data-testid="stSidebar"] {display: none;}  /* Hide the sidebar */
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Function to convert the image to base64 encoding
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set a JPG as the background of the page
def set_background_image(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f"""
    <style>
    [data-testid="stApp"] {{
    background-image: url("data:image/jpeg;base64,{bin_str}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_background_image('image2.jpg')

# Title
st.markdown("<div style='text-align: center;'><h1 style='color: #353535; font-size: 80px; font-family: Roboto;'>DIETARY OPTIONS</h1></div>", unsafe_allow_html=True)

# Subtitle
st.markdown("<div style='text-align: center;'><h1 style='color: #353535; font-size: 20px; font-family: Roboto;'>"
            "Welcome to the Affordable Healthy Eating Resources program! Our mission is to empower communities by providing access to affordable, nutritious food options and resources that promote healthy eating habits for all."
            "</h1></div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center;'><h1 style='color: #353535; font-size: 20px; font-family: Roboto;'>"
            "Are you ready?"
            "</h1></div>", unsafe_allow_html=True)

# Custom button style with full-page centering
custom_button_style = """
    <style>
    div.stButton {
        text-align: center; /* Center the button container */
    }
    div.stButton > button {
        background-color: #353535;
        color: white;
        padding: 10px 20px;
        font-size: 30px;
        border: none;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #000000;
        color: white;
    }
    </style>
    """
# Apply the custom style
st.markdown(custom_button_style, unsafe_allow_html=True)

# Button with action
if st.button('START'):
    switch_page("questionaire")  # Corrected spelling here

# Footer
st.markdown("<div style='text-align: right;'><h1 style='color: #353535; font-size: 12px; font-family: Roboto;'>"
            "Powered by Gemini"
            "</h1></div>", unsafe_allow_html=True)
