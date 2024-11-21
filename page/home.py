import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64
from Modules import VisualHandler

# Cài đặt trang
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Khởi tạo giao diện
VisualHandler.initial()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background():
    """Đặt hình nền cho trang Home"""
    img = get_img_as_base64("home3.png")
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: local;
    }}
    </style>
    """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

def display_home():
    """Hiển thị nội dung trang Home"""
    st.markdown("""
    <div style='text-align: left; font-size: 36px; font-weight: bold;'>
        <div style="position: relative; top: -30px; font-size: 48px; font-weight: bold; margin-bottom: -10px;">
            CALM KITCHEN
        </div>
        <div style="width: 100px; height: 2px; background-color: white; margin: 10px 0;"></div>
        TIỆN LỢI <br>
        TIẾT KIỆM THỜI GIAN <br>
        DINH DƯỠNG TRONG MỌI BỮA ĂN
    </div>
    """, unsafe_allow_html=True)
    set_background()

# Hiển thị phần nội dung trang Home
display_home()



# Nhúng CDN Font Awesome để sử dụng icon mạng xã hội
st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# Hiển thị footer
def display_footer():

    st.markdown("""
    <footer style="background-color: rgba(0, 0, 0, 0.7); padding: 20px; text-align: center; color: white; position: fixed; bottom: 0; left: 0; width: 100%; z-index: 9999;">
        <div style="font-size: 24px; font-weight: bold;">
            CALM KITCHEN™
        </div>
        <div>
            <a href="https://www.facebook.com/profile.php?id=61567855092141&is_tour_dismissed" target="_blank">
                <i class="fab fa-facebook" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.instagram.com/_calm_kitchen_/" target="_blank">
                <i class="fab fa-instagram" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://twitter.com" target="_blank">
                <i class="fab fa-twitter" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.youtube.com/@gordonramsay" target="_blank">
                <i class="fab fa-youtube" style="font-size: 24px; margin: 10px;"></i>
            </a>
            <a href="https://www.linkedin.com" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 24px; margin: 10px;"></i>
            </a>
        </div>
        <div style="margin-top: 10px;">
            <a href="/about_us" style="margin-right: 20px; text-decoration: none; color: white;">About Us</a>
            <a href="/contact_us" style="text-decoration: none; color: white;">Contact Us</a>
        </div>
        <div style="margin-top: 20px; font-size: 14px; color: #bbb;">
            Copyright © Group 3 - DSEB 65B
        </div>
    </footer>
    """, unsafe_allow_html=True)

# Hiển thị phần footer
display_footer()