import streamlit as st
import base64
from streamlit_extras.switch_page_button import switch_page
import toml

class VisualHandler:
    # Danh sách hình ảnh nền
    BACKGROUND_OPTIONS = [
        "backgrounds/bg1.jpg",
        "backgrounds/bg2.jpg",
        "backgrounds/bg3.jpg",
        "backgrounds/bg4.jpg",
        "backgrounds/bg5.jpg",
    ]
    
    @staticmethod
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    @classmethod
    def set_background(cls, image):
        background = cls.get_img_as_base64(image)
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{background}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)

    @classmethod
    def load_css(cls, css: str):
        with open(css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    @classmethod
    def handle_sidebar_style(cls):
        with st.sidebar:
            # Nếu st.session_state.css chưa có giá trị, gán giá trị mặc định cho nó
            if "css" not in st.session_state:
                st.session_state.css = "style.css" 
            VisualHandler.load_css(st.session_state.css)
        
        # Hiển thị logo của bạn mà không sử dụng 'class_'
        st.sidebar.image("logo.png", use_column_width=True, caption=None)

        # Chọn hình nền
        st.sidebar.title("Chọn hình nền")
        selected_background = st.sidebar.selectbox(
            "Chọn hình ảnh nền:", 
            cls.BACKGROUND_OPTIONS,
            format_func=lambda x: x.split("/")[-1].replace(".jpg", "").replace("_", " ").title()
        )

        # Cập nhật nền nếu người dùng chọn hình mới
        if "bg" not in st.session_state or st.session_state.bg != selected_background:
            st.session_state.bg = selected_background
            cls.set_background(selected_background)

    @classmethod
    def display_sidebar_features(cls):
        # Các nút chuyển trang
        st.sidebar.title("Chức năng")
        if st.sidebar.button("Home"):
            switch_page("Home")
        if st.sidebar.button("About Us"):
            switch_page("About Us")
        if st.sidebar.button("Contact Us"):
            switch_page("Contact Us")
        if st.sidebar.button("Recipe"):
            switch_page("Recipe")
        if st.sidebar.button("Make Menu"):
            switch_page("Make Menu")

        st.sidebar.divider()

        st.sidebar.markdown("""
        - **Email**: calmkitchen@gmail.com
        - **Phone**: +84 123 456 789
        - **Address**:  Phòng 712, Tòa nhà A2, Trường Đại học Kinh Tế Quốc Dân, 207 Đường Giải Phóng, Quận Hai Bà Trưng, Hà Nội.
        """)
        
        st.sidebar.divider()

        st.sidebar.markdown('<div style="text-align: center">© 2024 by Group 3 - DSEB 65B</div>', unsafe_allow_html=True)

    @classmethod
    def initialize_session_state(cls):
        """Khởi tạo trạng thái ứng dụng."""
        if "bg" not in st.session_state:
            st.session_state.bg = cls.BACKGROUND_OPTIONS[0]

        # Khởi tạo giá trị cho thuộc tính 'css' nếu chưa có
        if "css" not in st.session_state:
            st.session_state.css = "style.css"  

    @classmethod
    def initial(cls):
        """Khởi tạo toàn bộ giao diện."""
        cls.initialize_session_state()
        cls.handle_sidebar_style()  
        cls.display_sidebar_features() 
        if st.session_state.bg:
            cls.set_background(st.session_state.bg)
