
import streamlit as st
import main,manage,credential,login
from streamlit_authenticator import *
#auth
sidebar = st.sidebar.radio(
    "sidebar",
    ("main", "users", "manage", "credential")   
)
#check login


#sidebar
if sidebar == 'main':
    if login.check_login():
        main.main()
elif sidebar == "manage":
    if login.check_login():
        manage.manage()
elif sidebar == 'users':
    if login.check_login():
        tab1, tab2, tab3 = st.tabs(["addusers", "updateusers", "resetpassword"])
        authenticator,username,config = login.get_data()
        with tab3:
            st.header("resetpassword")
            if st.session_state['authentication_status']:
                try:
                    if authenticator.reset_password(username, 'Reset password'):
                        st.success('Password modified successfully')
                        with open('config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                except Exception as e:
                    st.error(e)

        with tab2:
            st.header("updateusers")
            if st.session_state['authentication_status']:
                try:
                    if authenticator.update_user_details(username, 'Update user details'):
                        st.success('Entries updated successfully')
                        with open('config.yaml', 'w') as file:
                            yaml.dump(config, file, default_flow_style=False)
                except Exception as e:
                    st.error(e)

        with tab1:
            st.header("addusers")
            try:
                if authenticator.register_user('Register user', preauthorization=False):
                    st.success('User registered successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
        st.write(config)
elif sidebar == 'credential':
    if login.check_login():
        credential.credential()
