import streamlit as st
import pandas as pd
from PIL import Image
import base64

def click_listen():
    st.session_state['listen_clicked'] = True
    Radio_url = data[data["Station"] == selected_station].values.tolist()[0][2][2:-1]
    st.audio(Radio_url, format="audio/mp3", autoplay=True)
    

im = Image.open("./Source/favicon.ico")
# Configure the main page
st.set_page_config(
    page_title="Listen On-Line Radio Stations",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': 'mailto:papavask@yahoo.com',
        'About': "# Listen music for entertainment* On line radio statios"
    }
)

image_url = "./Source/bg-img.jpg"  # Or use a local path like "assets/background.jpg"
mime_type = image_url.split('.')[-1:][0].lower()
with open(image_url, "rb") as f:
   content_bytes = f.read()
content_b64encoded = base64.b64encode(content_bytes).decode()
bg_url = f'data:image/{mime_type};base64,{content_b64encoded}'


st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("{bg_url}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-color: #61dafb; /* Dark background */
            color: #282c34;            /* Light blue text */
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
        
# Set title
st.title("On-Line Radio Stations")

subheader = st.subheader("Have Fun with music\nInstructions:")

# Set text
st.write("Welcome to the On-Lne Radio portal!")
st.write("Use the dropdown menus to select a station,\n\nand then click the button to start listening.")


# insert image
#st.image("assets/picture.jpg")

file_path = "./Source/RadioList.csv"

data = pd.read_csv(file_path, sep=",")

station_list = list(data["Station"])
st.session_state['listen_clicked'] = False
# Select station
selected_station = st.sidebar.selectbox(
                   "Select a station from the list",
                   station_list
                   )
st.button("Listen Music", key="listen", on_click=click_listen)
st.button("Find Title", key="title")


if st.session_state['listen_clicked']:
    if st.button('title'):
        st.write("butt02 was clicked!")
else:
    st.button("Find Title", disabled=True)
    

