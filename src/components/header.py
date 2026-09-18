import streamlit as st 


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-item:center; justify-content:center; margin-bottom:15px; margin-top:30px;">
            <img src='{logo_url}' style='height:100px; display:flex; flex-direction:column; align-item:center; justify-content:center; ' />
            <h1 style='text-align:center; color:#F2EFE7'>SNAP <br>CLASS</h1> 
        </div>    
        """,unsafe_allow_html=True)

def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; align-item:center; justify-content:center;text-align:center; gap:15px;margin-top:10px">
            <img src='{logo_url}' style='height:90px; margin-top:10px' />
            <h2 style='color:#66A3BF ; '>SNAP <br>CLASS</h2> 
        </div>    
        """,unsafe_allow_html=True)    