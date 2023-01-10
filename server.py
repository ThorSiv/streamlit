
import streamlit as st
import main,manage,credential
from streamlit_authenticator import *
#auth
sidebar = st.sidebar.radio(
    "sidebar",
    ("main", "users", "manage", "credential")   
)
#check login
with open('config.yaml') as f:
    config = yaml.load(f,Loader=SafeLoader)
authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
global name, authentication_status, username
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout("logout","sidebar")

    # # st.write(f'Welcome *{name}*')
    # # st.title('Some content')
    # st.write("You have login")
    
elif authentication_status == False:
    st.error('Username/password is incorrect')
    
elif authentication_status == None:
    st.warning('Please enter your username and password')

#sidebar
if sidebar == 'main':
    if authentication_status:
        main.main()
elif sidebar == "manage":
    if authentication_status:
        manage.manage()
elif sidebar == 'users':
    if authentication_status:
        tab1, tab2, tab3 = st.tabs(["addusers", "updateusers", "resetpassword"])

        with tab3:
            st.header("resetpassword")
            if authentication_status:
                try:
                    if authenticator.reset_password(username, 'Reset password'):
                        st.success('Password modified successfully')
                except Exception as e:
                    st.error(e)

        with tab2:
            st.header("updateusers")
            if authentication_status:
                try:
                    if authenticator.update_user_details(username, 'Update user details'):
                        st.success('Entries updated successfully')
                except Exception as e:
                    st.error(e)

        with tab1:
            st.header("addusers")
            try:
                if authenticator.register_user('Register user', preauthorization=False):
                    st.success('User registered successfully')
            except Exception as e:
                st.error(e)
elif sidebar == 'credential':
    if authentication_status:
        credential.credential()
