import streamlit as st 
from src.database.db import supabase
from src.database.db import enroll_student_to_subject
import time 
from src.database.db import create_attendance


def show_attendance_results(df,logs):
    st.write("Please Review attendance before confirm.")
    st.dataframe(df,hide_index=True ,width='stretch')
    
    col1 , col2 = st.columns(2)

    with col1 :
        if st.button("Discard", width='stretch',type='secondary'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save',width='stretch',type='tertiary'):
            try:
                create_attendance(logs)
                st.toast("Attendance Taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error('Sync Failed!')



@st.dialog("Attendance Records")
def attendance_result_dialog(df , logs):
    show_attendance_results(df,logs)
    