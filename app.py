import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RAPTOR Flowchart — AI-NIDS",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {padding: 0rem !important; max-width: 100% !important;}
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=1050, scrolling=True)
