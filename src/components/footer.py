import streamlit as st 


def footer_home():
    # logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="gap:6px ; display:flex; flex-direction:column; align-item:center; justify-content:center; text-align:center; margin-bottom:30px; margin-top:2rem;">
           <p style="font-weight:bold; color:white;">Created by Ranjeet kumar </p>    
        </div>    
        """,unsafe_allow_html=True)