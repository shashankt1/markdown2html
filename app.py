import streamlit as st
from converter import convert_markdown

st.title("🧠 Intelligent Markdown to HTML")
uploaded = st.file_uploader("Upload a Markdown file", type=["md"])

if uploaded:
    md = uploaded.read().decode("utf-8")
    html = convert_markdown(md)
    st.markdown(html, unsafe_allow_html=True)