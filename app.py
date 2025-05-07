import streamlit as st

with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

st.components.v1.html(html_content, height=600, scrolling=True)
