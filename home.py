import streamlit as st
import os
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background():
    img = get_img_as_base64("home3.png")
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-repeat: repeat;
        background-attachment: local;
        }}
        </style>
        """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

def display_home():
    
    st.markdown("""
    <div style='width: 100px; height: 2px; background-color: white; margin: 10px 0;'></div>
    <div style='text-align: left; font-size: 36px; font-weight: bold;'>
    TIỆN LỢI <br>
    TIẾT KIỆM THỜI GIAN <br>
    DINH DƯỠNG TRONG MỌI BỮA ĂN
    </div>
    """, unsafe_allow_html=True)
    set_background()


display_home()