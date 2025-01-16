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
    "Welcome to the On-Lne Radio portal!\nUse the dropdown menus below to select a station,\n\nand then click the button to start listening."
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
    Radio_url_df = data[data["Station"] == selected_station]
    Radio_url_list = Radio_url_df.values.tolist()
    Radio_url = Radio_url_list[0][2]
    st.write(selected_station +"\n\n")
    st.write(Radio_url)
    pass

if st.button("Stop listening"):
    player.stop()

# insert image
#st.image("assets/picture.jpg")
