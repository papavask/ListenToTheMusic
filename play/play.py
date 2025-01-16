import streamlit as st

# URL of the internet radio station (for example, a radio station's stream URL)
radio_url = "https://stream.starfm.de/ballads/mp3-128/"  # Replace with the desired radio stream URL

# Display the title of the app
st.title("Internet Radio Station Player")

# Provide some description or instructions
st.markdown("""
    This Streamlit app allows you to listen to an internet radio station. 
    Simply press the play button below to start streaming the radio station.
""")

# Display the audio player to stream the radio station
st.audio(radio_url, format="audio/mp3")

