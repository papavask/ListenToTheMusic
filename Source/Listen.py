import streamlit as st
import pandas as pd

# Configure the main page
st.set_page_config(
    page_title="Listen On-Line Radio Stations",
    page_icon="📊",
    layout="wide",
)

# Set title
st.title("On-Line Radio Stations")

subheader = st.subheader("Have Fun with music\nInstructions:")

# Set text
st.write(
    "Welcome to the On-Lne Radio portal! Use the dropdown menus below to select a station, and then click the button to start listening."
)

file_path = "./Source/RadioList.csv"

data = pd.read_csv(file_path, sep=",")

station_list = list(data["Station"])

    # Select company
selected_station = st.sidebar.selectbox(
                   "Select a station from the list",
                   station_list
                   )

if st.button("Listen Music"):
  pass

# insert image
#st.image("assets/picture.jpg")
