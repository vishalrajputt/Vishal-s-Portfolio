import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Vishal.Data",page_icon=":four_leaf_clover:",layout="wide")

# defined a obj to fetch lottie url
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

coding_gif= load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")

# header section-----------

with st.container():
    st.subheader("Hi, I am Vishal :wave:")
    st.title("A Data Analyst from India")

    st.write("I am passionate about finding ways to use Python to uncover insights, identify patterns and trends, and support decision-making processes for businesses.")
    st.write("[Learn more >](https://www.linkedin.com/in/rajput-vishal-singh-a24067237/)")

# what i do ---------------

with st.container():
    st.write('---')
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write( """
        
        I have been working in data analysis for several years and have a strong track record of delivering insightful and actionable solutions to business problems. I am an expert in using statistical and analytical techniques to extract meaning from complex data sets and have experience with a variety of data analysis tools and methods. My expertise extends throughout the entire data analysis process, from data gathering and cleaning to data visualization and presentation of results. I am dedicated to providing my clients with the best possible solutions to their data-related challenges.
        
        My Interests are:

        Machine Learning| Deep Learning| Computer Vision| Statistical analysis


        """)

        st.write("[Github->](https://github.com/vishalrajputt)")
    with right_column:
        st_lottie(coding_gif,height=300,key="coding")
     

    with st.container():
        st.header("My Projects")

        
    




