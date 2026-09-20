import streamlit as st 

def style_background_home():
    st.markdown("""
         <style>
               .stApp{
                    background-color: rgb(216, 230, 238) !important;
                }

               .stApp div[data-testid="stColumn"]{
                    background-color: white !important;
                    padding:2.5rem !important;
                    border-radius:3.5rem !important;
                    box-shadow:0 8px 20px rgba(0,0,0,0.12) !impo
               } 
            </style>  
                """ 
                , unsafe_allow_html=True)
    
def style_background_dashboard():
    st.markdown("""
         <style>
               .stApp{
                    background-color: rgb(216, 230, 238) !important;

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
               font-size:2.7rem !important;
               line-height:0.9 !important;
               margin-bottom:0rem !important;
               color:#1A2B4C !important;
            }    
            
            h2 {
                font-family: 'Valley Sans' , 'sans-serif' !important;
                font-size:2.7rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color:#1A2B4C !important;
            } 
            h3 ,h4 ,p {
                font-family: 'Outfit','sans-serif';
             }

            button{
                border-radius:1.5rem !important;
                background-color:#FF6B4A !important;
                color:#FFFFFF !important;
                font-weight:bold !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            } 

            button[kind='secondary']{
                border-radius:1.5rem !important;
                font-weight:600 !important;
                font-size:2.5rem !important;
                background-color:#2ECC9B !important;
                color:#FFFFFF !important;
                font-weight:bold !important;
                padding:10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind='tertiary']{
                border-radius:1.5rem !important;
                background-color:#8B7FF0 !important;
                color:#FFFFFF !important;
                padding:10px 20px !important;
                font-weight:bold !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            } 
            button:hover{
                transform :scale(1.05)
                color:#E85A3A  !important;
            }
        </style>  
                """ 
                , unsafe_allow_html=True)