import streamlit as st
import mysql.connector
import pandas as pd
def main():
    with st.sidebar:
        st.write('I am in sidecar')
    col1, col2, col3 = st.columns(3)
    with col1:
        cluster = st.selectbox(
            'clusters',
            ('cluster1', 'cluster2', 'cluster3'))
    with col2:
        namespace = st.selectbox(
            'namespaces',
            ('default', 'test', 'pro'))
    with col3:
        resources = st.selectbox(
            'resources',
            ('deploy', 'configmap', 'daemonset','ingress'))
    mydata = pd.DataFrame(
        {
            "name":['lisa','bob','thor'],
            'podname':['test','clc','api'],
            'podip':['912','232','4433']
        }
    )
    st.dataframe(mydata,710)