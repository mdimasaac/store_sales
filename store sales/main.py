import streamlit as st
import pandas as pd
import snowflake.connector
from admin_page import admin_page
from overview import overview
from planning import planning
from user_page import user_page
st.set_page_config(page_title="Main", page_icon=":grins:", layout="wide", initial_sidebar_state="collapsed")
def main():
    st.write('<div style="text-align: center; color: yellow;"><h1>Store IT</h1></div>', unsafe_allow_html=True)
    options = ["Main","User Page","Admin Page","Overview", "Planning"]
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    

    if choice == "Main":
        st.text("main")
        pass
    elif choice == "User Page":
        cart = pd.read_csv("cart.csv")
        user_page(cart)
        pass
    elif choice == "Admin Page":
        admin_page()
        pass
    elif choice == "Overview":
        overview()
        pass
    elif choice == "Planning":
        planning()
        pass
main()