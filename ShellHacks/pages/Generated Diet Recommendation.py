import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64


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

# Add content
st.markdown("<div style='text-align: center;'><h1 style='color: #353535;'>Diet Recommendation:</h1></div>", unsafe_allow_html=True)

import streamlit as st

# Check if the diet recommendation is in session state
if 'diet_recommendation' in st.session_state:
    #st.markdown("<h2 style='color: #353535; font-size: 20px;'>Diet Recommendation:</h2>", unsafe_allow_html=True)
    st.markdown( f"<div style='color: #353535; font-size: 20px; line-height: 1.5;'>{st.session_state['diet_recommendation']}</div>", unsafe_allow_html=True)
    #st.markdown(f"<p style='color: #353535; font-size: 20px;'>{st.session_state['diet_recommendation']}</p>", unsafe_allow_html=True)
else:
    st.markdown("<h2 style='color: #353535; font-size: 20px;'>No diet recommendation available.</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #353535; font-size: 20px;'>Please go back and enter your details.</p>", unsafe_allow_html=True)


#go back to questionaire button
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
if st.button('Go back to QUESTIONAIRE'):
    switch_page("Questionaire")



st.markdown("<div style='text-align: right;'><h1 style='color: #353535; font-size: 12px; font-family: Roboto;'>"
            "Powered by Gemini"
            "</h1></div>", unsafe_allow_html=True)
