import streamlit as st
def manage():
    st.title('video...')
    video_file = open('big_buck_bunny.mp4', 'rb')
    video_bytes = video_file.read()

    st.video(video_bytes)