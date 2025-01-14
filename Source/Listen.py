import streamlit as st
import pandas as pd
from app.core.utilities import dropdown_menus
from core.excel import run_excel

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

file_path = "./Source/Stations.csv"

data = pd.read_csv(file_path, sep=",")

selected_station = dropdown_menus(
    station_label="Select Station",
    company_options=data["station"].unique(),
    default_company="---",
)

if st.button("Listen Music"):
  continue

# insert image
st.image("assets/picture.jpg")
