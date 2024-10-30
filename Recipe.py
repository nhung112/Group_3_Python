# PART 1
import streamlit as st
import json


with open("ingredients.json", "r", encoding="utf-8") as file:
    ingredients_data = json.load(file)

st.title("Chọn Nguyên Liệu")

# Khởi tạo danh sách để lưu các nguyên liệu đã chọn
selected_ingredients = []

# Duyệt qua từng loại nguyên liệu trong JSON
for category, items in ingredients_data.items():
    st.subheader(category)  # Tạo tiêu đề cho mỗi nhóm nguyên liệu
    cols = st.columns(5)  # Số cột trong lưới nút (tùy chỉnh theo nhu cầu)

    # Duyệt qua từng nguyên liệu và tạo các nút chọn
    for i, ingredient in enumerate(items):
        if cols[i % 5].checkbox(ingredient):
            selected_ingredients.append(ingredient)

# Hiển thị các nguyên liệu đã chọn
if selected_ingredients:
    st.write("Nguyên liệu đã chọn:", selected_ingredients)
else:
    st.write("Hãy chọn các nguyên liệu bạn có sẵn.")
