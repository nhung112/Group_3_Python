import streamlit as st
import base64
from st_pages import add_page_title, get_nav_from_toml
import webbrowser 
from streamlit_option_menu import option_menu

def main():
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav)
    add_page_title(pg)
    pg.run()
    

if __name__ == "__main__":
    main()