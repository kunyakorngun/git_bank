import streamlit as st 

color_selected = st.color_picker(label='', label_visibility='collapsed')
st.write(color_selected)
