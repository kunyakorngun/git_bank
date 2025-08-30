import streamlit as st 
import pandas as pd
from numpy.random import default_rng as rng
from collections import Counter

if 'all_records' not in st.session_state:
    st.session_state.all_records = {}
    
st.title("Color Picker")

with st.form(key="form1"):
    col1, col2 = st.columns([9,1], vertical_alignment="center")
    with col1:
        selected_name = st.text_input("Name")
    with col2:
        selected_color = st.color_picker("color", label_visibility="hidden", width="stretch")

    if st.form_submit_button("Summit"):
        if selected_name:
            st.session_state.all_records[selected_name] = selected_color

if st.session_state.all_records != {}:
    data = list(st.session_state.all_records.values())
    count_color = Counter(data)
    x, y = zip(*count_color.items())
    df = pd.DataFrame({"shade": x, "Amount": y, "color": x})
    st.bar_chart(df, x="shade", y="Amount", color="color")
print(data)