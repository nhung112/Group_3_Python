# PART 2
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import base64
import webbrowser
import re
import smtplib
import random
import pandas as pd
import json
from Modules import VisualHandler



st.set_page_config(
    page_title="Make Menu",
    page_icon="🍽",
    layout="wide",
    initial_sidebar_state="collapsed",
)
VisualHandler.initial()

# Load data files
foods_file_path = 'foods.csv'
ingredients_file_path = 'ingredients.json'
# Load data
foods_df = pd.read_csv(foods_file_path)
with open(ingredients_file_path, 'r', encoding='utf-8') as f:
    ingredients = json.load(f)

# Update column names based on actual CSV structure
food_name_column = 'Tên món'
calories_column = 'Calo '

########################################################################################################################################
st.title("Tính toán chỉ số BMI")

st.header("Thông tin cá nhân")
name = st.text_input("Họ và tên:")
age = st.number_input("Tuổi:", min_value=1, max_value=100, step=1)
gender = st.selectbox("Giới tính:", options=["Nam", "Nữ", "LGBT"])
height = st.number_input("Chiều cao (cm):", min_value=0.0, step=0.1)
weight = st.number_input("Cân nặng (kg):", min_value=0.0, step=0.1)
issue = st.multiselect("Bệnh lý( nếu có ):",  options=["Tiểu đường", "Huyết áp cao", "Dạ dày", "Gout"])
duration = st.selectbox("Chọn thời gian thực đơn:", options=["1 bữa", "1 ngày", "1 tuần", "1 tháng"])
def calculate_bmi(weight, height):
    if height > 0:
        height_m = height / 100  
        bmi = weight / (height_m ** 2)
        return bmi
    else:
        return None

def classify_bmi(bmi):
    if age >= 18:
        if bmi < 18.5:
            return "Thiếu cân"
        elif 18.5 <= bmi < 24.9:
            return "Cân nặng bình thường"
        else:
            return "Thừa cân"
    else:     
        if bmi < 15:
            return "Thiếu cân"
        elif 15 <= bmi < 25:
            return "Cân nặng bình thường"
        else:
            return "Thừa cân"

########################################################################################################################################
# Sample dishes based on BMI categories with calorie filtering
def get_menu_by_bmi(bmi_category):
    menu = []
    if bmi_category == "Thiếu cân":
        # Select dishes with at least 400 calories
        menu = foods_df[foods_df[calories_column] >= 400][[food_name_column, calories_column]].to_dict(orient='records')
    elif bmi_category == "Cân nặng bình thường":
        # Select all dishes without calorie restriction
        menu = foods_df[[food_name_column, calories_column]].to_dict(orient='records')
    elif bmi_category == "Thừa cân":
        # Select dishes with fewer than 400 calories
        menu = foods_df[foods_df[calories_column] < 400][[food_name_column, calories_column]].to_dict(orient='records')
    return [{"name": dish[food_name_column], "calories": dish[calories_column]} for dish in menu]

# Filter dishes based on health issue
def filter_by_health_condition(menu, issue):
    # If "None" is in issue, skip filtering
    if "None" in issue:
        return menu  # Return the menu as-is if no health issue are specified

    filtered_menu = []
    for dish in menu:
        is_allowed = True
        for ingredient in dish["name"].split():
            for condition in issue:
                if condition.strip() in foods_df.columns:
                    condition_filter = foods_df[foods_df[food_name_column] == ingredient]
                    if not condition_filter.empty and condition_filter[condition.strip()].values[0] == 1:
                        is_allowed = False
                        break
            if not is_allowed:
                break
        if is_allowed:
            filtered_menu.append(dish)  # Append the full dish dictionary
    return filtered_menu

# Generate menu with a clear breakfast filtering process
def generate_menu(duration, menu):
    daily_structure = {"Breakfast": [], "Lunch": [], "Dinner": []}
    
    # Filter menu for starch and vegetable dishes for Breakfast
    breakfast_menu = [dish for dish in menu if any(ingredient in dish["name"] for ingredient in ingredients.get("Tinh bột", []))]

    if duration == "1 bữa":
        return random.sample(menu, 2)  # Two unique dishes for a single meal
    elif duration == "1 ngày":
        if breakfast_menu:  # Check if there are breakfast options available
            daily_structure["Breakfast"] = random.sample(breakfast_menu, 1)
        daily_structure["Lunch"] = random.sample(menu, 2)
        daily_structure["Dinner"] = random.sample(menu, 2)
        return daily_structure
    elif duration == "1 tuần":
        weekly_menu = []
        for _ in range(7):
            day = {}
            if breakfast_menu:
                day["Breakfast"] = random.sample(breakfast_menu, 1)  
            day["Lunch"] = random.sample(menu, 2)
            day["Dinner"] = random.sample(menu, 2)
            weekly_menu.append(day)
        return weekly_menu
    elif duration == "1 tháng":
        monthly_menu = []
        for _ in range(30):
            day = {}
            if breakfast_menu:
                day["Breakfast"] = random.sample(breakfast_menu, 1) 
            day["Lunch"] = random.sample(menu, 2)
            day["Dinner"] = random.sample(menu, 2)
            monthly_menu.append(day)
        return monthly_menu
    
# Main function to create menu
def create_menu(weight, height, duration, issue):
    bmi = calculate_bmi(weight, height)
    bmi_category = classify_bmi(bmi)
    base_menu = get_menu_by_bmi(bmi_category)
    condition_filtered_menu = filter_by_health_condition(base_menu, issue)
    final_menu = generate_menu(duration, condition_filtered_menu)
    return final_menu

########################################################################################################################################
if st.button("Tính toán BMI"):
    bmi = calculate_bmi(weight, height)
    if bmi:
        st.write(f"Chỉ số BMI của bạn là: {bmi:.2f}")
        if age >= 18:
            classification = classify_bmi(bmi)
            st.write(f"Phân loại BMI (Người lớn): {classification}")
        else:
            classification = classify_bmi(bmi)
            st.write(f"Phân loại BMI (Trẻ em): {classification}")
    else:
        st.write("Vui lòng nhập chỉ số hợp lệ để tính toán BMI.")

if st.button("Generate Menu"):
    menu = create_menu(weight, height, duration, issue)
    st.write("### Suggested Menu:")
    bmi = calculate_bmi(weight, height)
    if bmi:  
        if duration == "1 tuần" or duration == "1 tháng":
            for day_idx, daily_menu in enumerate(menu, start=1):
                with st.expander(f"Day {day_idx}"):  # Mỗi ngày trong một hộp riêng
                    for meal, dishes in daily_menu.items():
                        st.subheader(meal)  # Hiển thị tên bữa ăn (Breakfast, Lunch, Dinner)
                        for dish in dishes:
                            st.write(f"- {dish['name']} ({dish['calories']} cal)")
                                
        elif duration == "1 bữa":
            st.subheader("Your Meal:")
            selected_dishes = random.sample(menu, 2)
            for dish in selected_dishes:
                st.write(f"- {dish['name']} ({dish['calories']} cal)")
                    
        else:  # Trường hợp "1 ngày"
            for meal, dishes in menu.items():
                st.subheader(meal)  # Hiển thị tên bữa ăn
                for dish in dishes:
                    st.write(f"- {dish['name']} ({dish['calories']} cal)")
    else: 
        st.write("Vui lòng tính toán BMI trước khi tạo menu.")