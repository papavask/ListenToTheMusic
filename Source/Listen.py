import streamlit as st
import pandas as pd
from PIL import Image


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

st.markdown(
    f"""
    <style>
    .reportview-container {
        background: url("bg-img.jpj")
    }
    .sidebar .sidebar-content {
        background: url("sb-img.jpj")
    }
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

# Select station
selected_station = st.sidebar.selectbox(
                   "Select a station from the list",
                   station_list
                   )

if st.button("Listen Music"):
    Radio_url = data[data["Station"] == selected_station].values.tolist()[0][2][2:-1]
    st.audio(Radio_url, format="audio/mp3", autoplay=True)
    

