from streamlit_authenticator import *
import streamlit as st
def check_login():
    global name, authentication_status, username,authenticator,config
    with open('config.yaml') as f:
        config = yaml.load(f,Loader=SafeLoader)
    authenticator = Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    
    name, authentication_status, username = authenticator.login('Login', 'main')

    if authentication_status:
        authenticator.logout("logout","sidebar")

        # # st.write(f'Welcome *{name}*')
        # # st.title('Some content')
        # st.write("You have login")
        return True
    elif authentication_status == False:
        st.error('Username/password is incorrect')
        return False
    elif authentication_status == None:
        st.warning('Please enter your username and password')
        return False
def get_data():
    return authenticator,username,config