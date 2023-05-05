import streamlit as st
import pandas as pd
import snowflake.connector
from store_management import store_management
from business_analysis import business_analysis
from in_store import in_store
st.set_page_config(layout='wide')


def main():
    c1, c2, c3, c4 = st.columns([3,2,1.5,.8])
    with c1:
        st.write(" ")
    with c2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write('<div style="text-align: right; color: yellow;"><h5><em>Powered by:</em></h5></div>', unsafe_allow_html=True)
    with c3:
        st.image("./snowflake.png")
    with c4:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.image("./streamlit.png")
        
        
    st.write('<div style="text-align: center; color: yellow;"><h1>Store IT!</h1></div>', unsafe_allow_html=True)
    
    
    options = ["Main","In-Store","Store Management","Business Analysis"]
    choice = st.sidebar.selectbox("Menu",options, key = '1')
    

    if choice == "Main":
        st.write('<div style="text-align: center; color: yellow;"><h4><em>[ Main Page - Introduction ]</em></h4></div>', unsafe_allow_html=True)
        st.write("_________")
        st.write('<div style="text-align: left;"><h3><em>In-Store:</em></h3></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- See product details and search through product names and/or categories</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Execute & Record all in-store transactions</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Display store catalog</h5></div>', unsafe_allow_html=True)

        st.write("_________")
        st.write('<div style="text-align: left;"><h3><em>Store Management:</em></h3></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Monitor last transactions</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Display profit within specific months</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Identify profit for each product category</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Modify product price and quantity in inventory</h5></div>', unsafe_allow_html=True)
        st.write("_________")
        st.write('<div style="text-align: left;"><h3><em>Business Analysis:</em></h3></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Display automatically generated & updated reports</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Analyze sales on specific months</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Identify profitability on specific product category</h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left;"><h5>- Plot sales growth on specific product</h5></div>', unsafe_allow_html=True)
        st.write("_________")
        pass
    elif choice == "In-Store":
        st.write('<div style="text-align: center; color: yellow;"><h4><em>[ In-Store-App ]</em></h4></div>', unsafe_allow_html=True)
        cart = pd.read_csv("cart.csv")
        in_store(cart)
        pass
    elif choice == "Store Management":
        st.write('<div style="text-align: center; color: yellow;"><h4><em>[ Store Management ]</em></h4></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: center; color: yellow;"><h6><em>You need to log in as an owner / store manager to see this function.</em></h6></div>', unsafe_allow_html=True)
        cc1,cc2 = st.columns([1,3])
        password = st.text_input("Enter Password", type = "password")
        st.text("Password = Snowflake1234")
        if password == "Snowflake1234":
            st.success("Successfully Logged in.")
            store_management()
        pass
    elif choice == "Business Analysis":
        business_analysis()
        pass
main()