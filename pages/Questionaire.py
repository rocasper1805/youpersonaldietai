import streamlit as st
import base64
import os
from dotenv import load_dotenv
import google.generativeai as genai
from streamlit import switch_page

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

# Load the .env file and get the API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Check if API key is loaded
if not api_key:
    st.write("Error: API key not found.")
else:
    genai.configure(api_key=api_key)

    # Create the model configuration
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # Create the model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction= "Proffesional tone"
    )

    # Start a chat session with the model
    chat_session = model.start_chat(history=[])

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
st.markdown("<div style='text-align: center;'><h1 style='color: #353535;'>Let's start by answering some questions:</h1></div>", unsafe_allow_html=True)

#style
custom_input_style = """
    <style>
    div.stTextInput > label {
        color: #353535; /* Change the label color */
    }
    div.stTextInput > div > input {
        color: #353535; /* Change the input text color */
    }
    </style>
"""
#style select box
custom_select_style = """
    <style>
    div.stSelectbox > label {
        color: black; /* Change the label color */
    }
    div.stSelectbox > div > select {
        color: #353535; /* Change the select text color */
    }
    </style>
"""
# style num input
custom_number_input_style = """
    <style>
    /* Change the label color */
    div.stNumberInput > label {
        color: black ; /* Label color */
    }
    /* Change the input field text color and background */
    div.stNumberInput > div > input {
        color: #353535; /* Input text color */
        background-color: #353535; /* Background color */
        border: 1px solid #353535; /* Border color */
        border-radius: 5px; /* Rounded edges */
        padding: 10px;
    }
    </style>
"""

# Apply the custom style
st.markdown(custom_number_input_style, unsafe_allow_html=True)


# Apply the custom style
st.markdown(custom_input_style, unsafe_allow_html=True)

# Apply the custom style
st.markdown(custom_select_style, unsafe_allow_html=True)

# Inputs
name_input = st.text_input("Enter your name:")
weight_input = st.text_input("Enter your weight(in lbs):")
age_input = st. number_input( "Age", min_value=0, max_value=150, value=18, step=1)
gender_input = st.selectbox("Select your gender", ("Male", "Female", "Prefer not to say"))
activity_input = st.text_input("Enter your average hours of physical activity per week:")
dietary_needs = st.text_input("Enter your dietary needs (if none enter NA):")
dietary_restrictions = st.text_input("Enter your dietary restrictions (if none enter NA):")

custom_button_style = """
    <style>
    div.stButton {
        text-align: right; /* Center the button container */
    }
    div.stButton > button {
        background-color: #566e50;
        color: white;
        padding: 10px 20px;
        font-size: 30px;
        border: black;
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

# Button to submit the data to the Gemini API
if st.button("Get Diet Recommendation"):
    if name_input and weight_input and gender_input:

        # Create input message for the model
        input_message = f"My name is {name_input}, my weight is {weight_input}, my age is {age_input}, my gender is {gender_input}, my average hours of physical activity per week is {activity_input}, my dietary needs are {dietary_needs}, my dietary restrictions are {dietary_restrictions}. Give me a 7 meal plan recommendation with low-cost food! I don't care about losing or gaining weight."

        try:
            # Sending the message to Gemini API or chat session
            response = chat_session.send_message(input_message)

            # Store the recommendation in session state
            st.session_state['diet_recommendation'] = response.text

            # Switch to page2
            switch_page("Generated Diet Recommendation.py")

        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please enter all required information (name, weight, gender, etc.).")

# # Button to submit the data to the Gemini API
# if st.button("Get Diet Recommendation"):
#     if name_input and weight_input and gender_input:
#
#         # Create input message for the model
#         input_message = f"My name is {name_input}, my weight is {weight_input}, my age is {age_input}, my gender is {gender_input}, my average hours of physical activity per week is {activity_input}, my dietary needs are {dietary_needs}, my dietary restrictions are {dietary_restrictions}. Give me a 7 meal plan recommendation with low-cost food! I don't care about losing or gaining weight."
#
#         try:
#             response = chat_session.send_message(input_message)
#
#             st.session_state['diet_recommendation'] = response
#          # Switch to page2
#             switch_page("/Users/pacoortiz/Desktop/ShellHacks/pages/Generated Diet Recommendation.py")
#         else:
#             st.write("Please enter all required information (name, weight, gender, etc.).")
st.markdown("<div style='text-align: right;'><h1 style='color: #353535; font-size: 12px; font-family: Roboto;'>"
            "Powered by Gemini"
            "</h1></div>", unsafe_allow_html=True)