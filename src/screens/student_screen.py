import streamlit as st
from src.ui.base_layout import style_background_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np 
from src.pipelines.face_recognition import face_recognition_models,get_face_embeddings ,predict_attendance ,train_classifier
from src.pipelines.voice_recognition import get_voice_embedding ,load_voice_encoder
from src.database.db import get_all_students ,create_student ,get_student_subjects, get_student_attendance ,unenroll_student_to_subject
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card

## student panel ------------------------
def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1,c2 = st.columns(2 , vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()

    with c2:
        st.subheader(f"""WELCOME ,{student_data['name']}""")
        if st.button("Logout",type='tertiary',key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1 , c2 = st.columns(2)

    with c1:
        st.header("Your Enrolled Subjects")
    with c2:
        if st.button('Enroll in Subject',type='primary',width='stretch'):
            enroll_dialog()    

    st.divider()

    with st.spinner('Loading Enrolled subjects...'):
        subjects= get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {'total':0,"attended":0}

        stats_map[sid]['total'] +=1

        if log.get('is_present'):
            stats_map[sid]['attended'] +=1

    cols = st.columns(2)
    for i ,sub_node in enumerate(subjects):
        sub =sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(sid , {'total':0,'attended':0})
        
        def unenroll_btn():
            if st.button("Unenroll from this course",key=f'unenroll_{sub['name']}' , type='tertiary',icon=':material/delete_forever:'):
                unenroll_student_to_subject(student_id , sid)
                st.toast(f"Unenrolled From {sub['name']} Succesfully")
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name = sub['name'],
                code = sub['subject_code'],
                section = sub['section'],
                stats = [
                    {'📅', 'Total',stats['total']},
                    {'✅', 'attended',stats['attended']},
                ],
                footer_callback = unenroll_btn
            )    

        
    footer_dashboard()

# student login panel by face or voice -----------------------------------

def student_screen():
    # header section --------------
    style_background_dashboard()
    style_base_layout()  

    if "student_data" in st.session_state:
        student_dashboard()
        return
      
    c1,c2 = st.columns(2 , vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()

    with c2:
        if st.button("GO Back",type='tertiary',key='loginbackbtn', shortcut='control+backspace'):
            st.session_state['login_type'] = None
            st.rerun()

    st.space()        
    st.header("Login using FaceID" , text_alignment='left')
    st.space()
    

    # main section ----------------------------
    show_registration = False
    photo_source =  st.camera_input("Position your face in the camera")

    # photo capture for login -------------------

    if photo_source :
        Image_np=  np.array(Image.open(photo_source))

        with st.spinner("AI is scanning..."):
          detected , all_ids , num_faces=  predict_attendance(Image_np)

          if num_faces == 0:
              st.warning('Face not found!')
          elif num_faces > 1:
              st.warning('Multiple faces found!')
          else:
              if detected:
                  student_id =list(detected.keys())[0]
                  all_students = get_all_students() 
                  student = next((s for s in all_students if s['student_id']  == student_id),None)

                  if student:
                      st.session_state.is_logged_in = True
                      st.session_state.user_role = 'student'
                      st.session_state.student_data = student
                      st.toast(f"Welcome Back!{student['name']}")
                      import time
                      time.sleep(1)
                      st.rerun()
              else:
                  st.info('Face not recognized! you might be a new student!')
                  show_registration = True 

    # Voice enrolled ---------------

    if show_registration:
        with st.container(border=True):
            st.header("Register New Profile")
            new_name = st.text_input("Enter your name")

            st.subheader('optional : Voice Enrollment')
            st.info("Enroll for voice only attendace ")

            audio_data = None
            try:
                audio_data  = st.audio_input('Recode a short phrase like I am present , My name is Akash.')
            except Exception :
                st.error("Voice not audiable , Record Again !") 

            if st.button('Create Account', type='tertiary'):
                if new_name:
                    with st.spinner('Creating Profile...'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(Image_np)

                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name , face_embedding=face_emb , voice_embedding = voice_emb)

                            if response_data:
                                train_classifier() 
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f"Profile creating! Hi {new_name}")
                                import time
                                time.sleep(1)
                                st.rerun()  
                            else:
                                st.error("Couldn't capture your facial feature for registration") 

                else:
                    st.warning("Please Enter your name!")


    # footer section --------------------------
    footer_dashboard()