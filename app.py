import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/GrapeLeaves.jpeg")
img_lottie_animation = Image.open("images/Koshari.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Raed :wave:")
    st.title("A computer Science Student From Egypt")
    st.write(
        "I am passionate about finding ways to use Python :snake: to develop and design Websites."
    )
    st.write("[Learn More >](https://www.python.org/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Home")
        st.write("##")
        st.write(
            """
            beside that I would like to talk about my country for a bit:
            - you may all know Egypt for its pyramids and the Sphinx but that's not all.
            - We have a rich culture from music to movies to food, specially the food (Koshari" :heart_eyes: ").
            If this sounds interesting to you, consider checking this video for interesting places to check around Egypt.
            """
        )
        st.write("[Amazing Places to visit in Egypt>](https://www.youtube.com/watch?v=BwNyfylA7do)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Egypt Foods ")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("The BEST Koshari in the world - Egyptian Vegan Street Food")
        st.write(
            """
            Koshari is Egyptian Vegan Street Food and the National Dish of Egypt. 
            I'm going to show you how to make the best koshari in the world. Better than you'd find it on any street corner in Cairo.
        
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=bGM2gh4bxmM)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Stuffed Grape vine Leaves the Egyptian way")
        st.write(
            """
            Stuffed Grape vine leaves, or Warak Enab are a classical middle eastern dish that is a must have at any dinner party. 
            They have a soft and tender texture, with a tangy herb rice filling, and today we'll be making them the Egyptian way which is Vegetarian and can easily be made Vegan!
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=vjwwga_NZMQ)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/Yourmail@yahoo.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
