import streamlit as st
import base64
from st_pages import add_page_title, get_nav_from_toml
    
def main():
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav, expanded= False)
    add_page_title(pg)
    pg.run()


    

if __name__ == "__main__":
    main()