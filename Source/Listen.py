import streamlit as st
import pandas as pd
from PIL import Image
import base64
import logging


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.user_ip = get_remote_ip()
        return super().filter(record)

def get_remote_ip() -> str:
    """Get remote ip."""
    try:
        ctx = get_script_run_ctx()
        if ctx is None:
            return None
        session_info = runtime.get_instance().get_client(ctx.session_id)
        if session_info is None:
            return None
    except Exception as e:
        return None
    return session_info.request.remote_ip


def click_listen(data, selected_station):
    # st.session_state.listen_clicked = True
    Radio_url = data[data["Station"] == selected_station].values.tolist()[0][2][2:-1]
    st.audio(Radio_url, format="audio/mp3", autoplay=True)
    st.write(st.session_state.listen_clicked)
    
def start_main():
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
    if 'listen_clicked' not in st.session_state:
       st.session_state.listen_clicked = False

    if 'selected_station' not in vars():
       st.session_state.listen_clicked = False

# Select station
    selected_station = st.sidebar.selectbox(
                       "Select a station from the list",
                       station_list
                       )
    if st.button("Listen Music", key="listen", on_click=click_listen, args=[data, selected_station]):
       st.session_state.listen_clicked = True
    # st.button("Find Title", key="title")
    st.write("Hi")
    st.write(st.session_state.listen_clicked)

    if st.session_state.listen_clicked:
        if st.button("Find Title"):
           text = st.sidebar.text_input("Text:")
           logger.info(f"This is the text: {text}")
           st.write("************************************butt02 was clicked!")
           logger.info("This is a logging test")
           logger.info(f"st.session_state.listen_clicked is {st.session_state.listen_clicked}!!!")
    else:
        st.button("Find Title", disabled=True)

def init_logging():
    # Make sure to instanciate the logger only once
    # otherwise, it will create a StreamHandler at every run
    # and duplicate the messages

    # create a custom logger
    logger = logging.getLogger("foobar")
    if logger.handlers:  # logger is already setup, don't setup again
        return
    logger.propagate = False
    logger.setLevel(logging.INFO)
    # in the formatter, use the variable "user_ip"
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s [user_ip=%(user_ip)s] - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.addFilter(ContextFilter())
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__ == "__main__":
    init_logging()
    logger = logging.getLogger("foobar")
    logger.info("Inside main")
    start_main()

