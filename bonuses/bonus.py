import streamlit as st
from PIL import Image


with st.expander("Start camera:"):
    cam_img = st.camera_input("Most handsome man below; ")

    if cam_img:
        img = Image.open(cam_img)

        gray_img = img.convert("L")
        st.image(gray_img)

uploaded_image = st.file_uploader("Upload Image", key="upload")

if uploaded_image:
    uploaded_img = Image.open(uploaded_image)
    uploaded_gray = uploaded_img.convert("L")
    st.image(uploaded_gray)


st.session_state
