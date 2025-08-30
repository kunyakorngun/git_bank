import streamlit as st 
import pandas as pd
from numpy.random import default_rng as rng
from collections import Counter

st.title("Color Picker")

data = ["#CD5C5C", "#F08080", "#FFA07A", "#CD5C5C"]
count_color = Counter(data)
# print(count_color)
x, y = zip(*count_color.items())

df = pd.DataFrame({"shade": x, "Amount": y, "color": x})
# st.bar_chart(df.set_index("Color"))
st.bar_chart(df, x="shade", y="Amount", color="color")
