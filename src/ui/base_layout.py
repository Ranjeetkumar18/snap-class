import streamlit as st 

def style_background_home():
    st.markdown("""
         <style>
               .stApp{
                    background:#3368A0 !important;
                }

               .stApp div[data-testid="stColumn"]{
                    background-color:#F2EFE7 !important;
                    padding:2.5rem !important;
                    border-radius:3.5rem !important;
               } 
            </style>  
                """ 
                , unsafe_allow_html=True)
    
def style_backgroun_dashboard():
    st.markdown("""
         <style>
               .stApp{
                    background:#C8DFDB

                }
            </style>  
                """ 
                , unsafe_allow_html=True)
    
def style_base_layout():
    st.markdown("""
         <style>
         @import url('https://fonts.googleapis.com/css2?family=Valley+Sans:ital,wght@0,900;1,900&display=swap');
         @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');  
          /* Hide Top Bar of streamlit */

            #MainMenu , footer , header {
                visibility: hidden;
            }
            .block-container{ 
                padding-top:1.5rem;    
                }
            
            h1 {
               font-family: 'Valley Sans' , 'sans-serif' !important;
               font-size:3rem !important;
               line-height:0.9 !important;
               margin-bottom:0rem !important;
               color:#4A4A4A !important;
            }    
            
            h2 {
                font-family: 'Valley Sans' , 'sans-serif' !important;
                font-size:3rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color:#4A4A4A !important;
            } 
            h3 ,h4 ,p {
                font-family: 'Outfit','sans-serif';
             }

            button{
                border-radius:1.5rem !important;
                background:#FFF9D8 !important;
                color:white !important;
                font-weight:bold !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            } 

            button[kind='secondary']{
                border-radius:1.5rem !important;
                font-weight:600 !important;
                font-size:2.5rem !important;
                background:#FF9D50 !important;
                color:black !important;
                font-weight:bold !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind='tertiary']{
                border-radius:1.5rem !important;
                background:#55E07E !important;
                color:black !important;
                padding:10px 20px !important;
                font-weight:bold !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            } 
            button:hover{
                transform :scale(1.05)
            }
        </style>  
                """ 
                , unsafe_allow_html=True)