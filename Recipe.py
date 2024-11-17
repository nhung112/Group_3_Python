#PART 1
import streamlit as st
import json
import pandas as pd

with open("ingredients.json", "r", encoding="utf-8") as file:
    ingredients_data = json.load(file)
medical_conditions = ["Tiểu đường", "Huyết áp cao", "Dạ dày", "Gout"]
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
    </style>
""", unsafe_allow_html=True)

selected_ingredients = []
selected_conditions = []
st.title("Gợi ý món ăn")
df = pd.read_csv("foods.csv")
def similarity(list1, list2):
    set1 = set(list1.split(","))
    set2 = set(list2)
    return len(set1.intersection(set2))

def link_create(ten_mon):
    row = df.loc[df['Tên món'] == ten_mon]
    return row['Công thức'].values[0]

display = False
with st.sidebar:
    st.title("Chọn nguyên liệu")
    for category, items in ingredients_data.items():
        st.markdown(f"**{category}**")
        ingredient_columns = st.columns(3)
        for i, ingredient in enumerate(items):
            with ingredient_columns[i % 3]:
                if st.checkbox(ingredient, key=f"{category}_{ingredient}"):
                    selected_ingredients.append(ingredient)

    st.title("Bệnh lý")
    condition_columns = st.columns(2)
    for i, condition in enumerate(medical_conditions):
        with condition_columns[i % 2]:
            if st.checkbox(condition, key=f"condition_{condition}"):
                selected_conditions.append(condition)

    button_column = st.columns([2, 1])  
    with button_column[1]: 
        if st.button("Xác nhận", key="confirm_button"):
            display = True
#            chosen_ingredients = {category: items for category, items in selected_ingredients.items() if items} 
if display:
            # Lọc dữ liệu
        #if selected_conditions:
            # Tạo một DataFrame tạm thời để chứa các điều kiện lọc
    if selected_conditions:
        conditions = [~(df[col] == 1) for col in selected_conditions]
        df_loc = df[pd.concat(conditions, axis=1).all(axis=1)]
    else:
        df_loc = df.copy()
    if not selected_ingredients:
        st.warning("Vui lòng chọn nguyên liệu mà bạn có.")
    else:
        # Tính độ trùng lặp và sắp xếp
        df["similarity"] = df["Nguyên liệu"].apply(lambda x: similarity(x, selected_ingredients))
        df_filtered = df[df["similarity"] > 0]

        if df_filtered.empty:
            st.info("CALM KITCHEN hiện tại chưa có món ăn phù hợp cho nguyên liệu của bạn.")
        else:
            df_filtered = df_filtered.sort_values("similarity", ascending=False)

        # Hiển thị kết quả
        cols = st.columns(3)
        for index, row in df_filtered.iterrows():
            col = cols[index % 3]
            with col:
                with st.container():
                    st.markdown(
                        f"""
                        <div style="background-color:#e0f7fa; padding: 20px; border-radius: 10px; 
                                    border: 2px solid #b0e0e6;">
                            <h3 style="color:#333;">{row[0]}</h3>
                            <p><strong>Nguyên liệu chính:</strong> {row[1]}</p>
                            <p><strong>Thời gian:</strong> {row[7]}</p>
                            <p><strong>Calo:</strong> {row[8]} kcal</p>
                            <a href="{link_create(row[0])}" target="_blank">
                                <button style="padding: 8px 12px; color: white; background-color: #4CAF50; 
                                            border: none; border-radius: 5px; cursor: pointer;">
                                    Xem công thức
                                </button>
                            </a>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                st.markdown("<br>", unsafe_allow_html=True)