import streamlit as st 

def main():

    st.header("This is main heading..")
    name = st.text_input("Enter here your query..")


    col1 ,col2 = st.columns(2)
    with col1:
        if st.button("Submit" ,type='primary',width='stretch'):
            print("hii" , name)
    with col2:
         st.button("click me!" ,type='primary',width='stretch')

    st.markdown ("""
         <style>
                button{
                    background:orange !important;
            }
            </style>
    """,unsafe_allow_html=True)      
main()    