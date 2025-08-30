import streamlit as st

if 'all_records' not in st.session_state:
    st.session_state.all_records = {}

with st.form(key="form1"):
    col1, col2 = st.columns([9,1], vertical_alignment="center")
    with col1:
        selected_name = st.text_input("Name")
    with col2:
        selected_color = st.color_picker("color", label_visibility="hidden", width="stretch")

    if st.form_submit_button("Summit"):
        if selected_name:
            st.session_state.all_records[selected_name] = selected_color

st.write(st.session_state.all_records)

