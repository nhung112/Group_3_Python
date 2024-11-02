import streamlit as st
import base64
from st_pages import add_page_title, get_nav_from_toml
import webbrowser
import re
import smtplib


st.title("Feedback Form:")

with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    Submit = st.form_submit_button("Submit")

email_regex = r"^[a-zA-Z0-9_.+-]+@(gmail).(com|edu|net|org)$"
if Submit:
    if not re.match(email_regex, email):
        st.error("Invalid email address")
    else:
        st.success("Form submitted successfully")

st.title("Contact us:")
facebook_url = "https://www.facebook.com/profile.php?id=100056612376153"  
instagram_url = "https://www.instagram.com/dchuy_006/?igsh=MTA0bHY3aXBucTdyag%3D%3D#"  
st.markdown(f"""
    <div style="display: flex; gap: 10px;">
        <a href="{facebook_url}" target="_blank">
            <button style="background-color: #3b5998; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                Go to Facebook Page
            </button>
        </a>
        <a href="{instagram_url}" target="_blank">
            <button style="background-color: #E1306C; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
                Go to Instagram Page
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)