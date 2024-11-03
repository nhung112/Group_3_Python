import streamlit as st
import json

# Load the ingredients data
with open("ingredients.json", "r", encoding="utf-8") as file:
    ingredients_data = json.load(file)

# Apply custom styling
st.markdown("""
    <style>
    .ingredient-box {
        display: inline-block;
        background-color: #ffffff; /* White background */
        color: #333;
        border: 2px solid #dcdcdc; /* Light gray border */
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        text-align: center;
        font-weight: bold;
        width: 100%;
        font-size: 18px;
    }
    .ingredient-box input[type="checkbox"] {
        accent-color: #4CAF50; /* Checkbox color */
        transform: scale(1.2); /* Make the checkbox slightly larger */
    }
    .section-heading {
        font-size: 24px;
        color: #333; /* Gray color */
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

with st.sidebar:
    st.markdown('<div class="section-heading">Chọn Nguyên Liệu</div>', unsafe_allow_html=True)
    selected_ingredients = {}
    
    for category, items in ingredients_data.items():
        with st.sidebar.expander(f"**{category}**", expanded=True):
            selected_ingredients[category] = []
            
            ingredient_columns = st.columns(3)
            for i, ingredient in enumerate(items):
                with ingredient_columns[i % 3]:  # Distribute ingredients in three columns
                    if st.checkbox(ingredient, key=ingredient):
                        selected_ingredients[category].append(ingredient)

    st.write("")
    col1, col2 = st.columns([2, 1])  
    with col1:
        st.write("")
    with col2:
        if st.button("Xác nhận", key="confirm_button"):
            chosen_ingredients = [ingredient for category in selected_ingredients.values() for ingredient in category]
        
    
st.markdown('<div class="section-heading">Gợi Ý Món Ăn</div>', unsafe_allow_html=True)
