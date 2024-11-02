#PART 1
import streamlit as st
import json


with open("ingredients.json", "r", encoding="utf-8") as file:
    ingredients_data = json.load(file)

st.markdown("""
    <style>
    .ingredient-box {
        display: inline-block;
        background-color: #f0f8ff;
        color: #333;
        border: 2px solid #90ee90;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        text-align: center;
        font-weight: bold;
        width: 100%; 
        font-size: 18px:
    }
    .ingredient-box input[type="checkbox"] {
        accent-color: #4CAF50; /* Checkbox color */
        transform: scale(1.2); /* Make the checkbox slightly larger */
    }
    .section-heading {
        font-size: 24px;
        color: #4CAF50;
        font-weight: bold;
        margin-top: 20px;
        text-align: center;
    }
    .category-title {
        font-size: 20px;
        color: #333;
        margin-top: 15px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 4])

with col1:
    st.markdown('<div class="section-heading">Chọn Nguyên Liệu</div>', unsafe_allow_html=True)
    selected_ingredients = {}
    
    for category, items in ingredients_data.items():
        st.markdown(f"<h3 class='category-title'>{category}</h3>", unsafe_allow_html=True)
        
        ingredient_columns = st.columns(3)
        for i, ingredient in enumerate(items):
            with ingredient_columns[i % 3]:
                selected_ingredients[ingredient] = st.checkbox(ingredient, key=ingredient)

    chosen_ingredients = [ingredient for ingredient, selected in selected_ingredients.items() if selected]

with col2:
    st.markdown('<div class="section-heading">Gợi Ý Món Ăn</div>', unsafe_allow_html=True) 