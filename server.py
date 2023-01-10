
import streamlit as st
import login,main
#auth
sidebar = st.sidebar.radio(
    "sidebar",
    ("main", "manage", "users", "credential")   
)


if sidebar == 'main':
    if login.check_login():
        main.main()
elif sidebar == "manage":
    if not login.check_login():
        sidebar= 'main'
    else:
        st.write('nice mange')
elif sidebar == 'users':
    if not login.check_login():
        sidebar = 'main'
    else:
        st.write('good users')
elif sidebar == 'credential':
    if not login.check_login():
        sidebar = 'main'
    else:
        st.write('good credentials')
