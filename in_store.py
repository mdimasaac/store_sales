def in_store(cart):
    import streamlit as st
    import pandas as pd
    import snowflake.connector
    from datetime import datetime
    from snowflake.snowpark import Session

    conn = snowflake.connector.connect(user = "mdimasaac", password = "Snowflake123", account = "vliobpf-yr09142",
                                    database = "store_it", schema = "store_schema")
    cur = conn.cursor()
    q_dflog = "select * from logistics"
    cur.execute(q_dflog)

    dflog = cur.fetch_pandas_all()
    # t1, t2, t3 = st.tabs(["Input","Catalog","Place Order"])
    t1,t2 = st.tabs(["Input","Catalog"])
    # ----------------------------------------------------------------------
    with t1:
        lname, lprice, lbuy, ltotal = [],[],[],[]
        notif = False
        col01,col03 = st.columns(2)
        # ----------------------------------------------------------------------
        with col01:
            name = st.radio("Search Product by:",("Category","Name"))
            if name == "Category":
                selected_category = st.selectbox("Category:", options=dflog['CATEGORY'].unique())
                selected_name = st.selectbox("Product Name:", options=dflog["PRODUCT_NAME"][dflog["CATEGORY"] == selected_category])
            elif name == "Name":
                selected_name = st.selectbox("Product Name:", options=dflog["PRODUCT_NAME"].sort_values(ascending = True))
        # ----------------------------------------------------------------------
        with col03:
            
            st.text("Product Name: "+selected_name)
            price = dflog["SELL_PRICE"][dflog["PRODUCT_NAME"]==selected_name].values.tolist()[0]
            st.text("Price per item\t: "+str(price)+"€")
            stock = dflog["STOCK"][dflog["PRODUCT_NAME"]==selected_name].values.tolist()[0]
            st.text("Available stock\t: "+str(stock))
            buy = st.selectbox("Buy:", options=range(0,stock+1))
            total = buy*price
            col11, col12 = st.columns(2)
            # ----------------------------------------------------------------------
            with col11:
                st.text("Total: "+str(total)+" €")
            # ----------------------------------------------------------------------
            with col12:
                add = st.button("Add to Cart")
                if add:
                    lname.append(selected_name)
                    lprice.append(price)
                    lbuy.append(buy)
                    ltotal.append(total)
                    cart2 = pd.DataFrame(columns=["Product Name","Price","Qty","Total"])
                    cart2["Product Name"] = lname
                    cart2["Price"] = lprice
                    cart2["Qty"] = lbuy
                    cart2["Total"] = ltotal
                    cart = pd.concat([cart,cart2], axis = 0)
                    notif = True
                    st.balloons()
        # ----------------------------------------------------------------------
        pd.set_option('display.max_colwidth', None)
        st.write("_________")
        st.subheader("Your Cart")
        if st.button("Empty the Cart"):
            cart = pd.DataFrame(columns=["Product Name","Price","Qty","Total"])
        if notif:
            st.success("Item added to cart!")
        st.dataframe(cart, width = 1400)
        subtotal = cart["Total"].sum()
        st.write("Sub Total: "+str(subtotal)+" €")
        confirm = st.button("Confirm Purchase")
        cart.to_csv("cart.csv",index = False)
        # ----------------------------------------------------------------------
        if confirm:
            for name in cart["Product Name"].tolist():
                dflog["STOCK"][dflog["PRODUCT_NAME"] == name] = dflog["STOCK"][dflog["PRODUCT_NAME"] == name] - cart["Qty"][cart["Product Name"] == name].values[0]
            cur.execute('''CREATE OR REPLACE TABLE logistics (product_name VARCHAR, product_id VARCHAR, category VARCHAR, buy_price FLOAT,
                    sell_price FLOAT, stock INTEGER, profit_per_item FLOAT)''')
            datalog = dflog.values.tolist()
            cur.executemany('''INSERT INTO logistics (product_name, product_id, category, buy_price, sell_price, stock, profit_per_item)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)''', datalog)
            q_column = "SELECT * FROM STORE_DATA LIMIT 1"
            cur.execute(q_column)
            qdf = cur.fetch_pandas_all()
            df_update = pd.DataFrame(columns = qdf.columns.tolist())
            for name in cart["Product Name"].tolist():
                q_df = "SELECT * FROM STORE_DATA WHERE PRODUCT_NAME = '"+name+"' LIMIT 1"
                cur.execute(q_df)
                qdf1 = cur.fetch_pandas_all()
                qdf1["QUANTITY"] = cart["Qty"][cart["Product Name"] == name].values[0]
                qdf1["SALES"] = qdf1["QUANTITY"]*qdf1["SELL_PRICE"]
                qdf1["PROFIT"] = qdf1["PROFIT_PER_ITEM"]*qdf1["QUANTITY"]
                qdf1["DATE"] = datetime.today().strftime('%Y-%m-%d')
                df_update = pd.concat([df_update, qdf1], axis = 0)
        # ----------------------------------------------------------------------
# appending new row to existing snowflake database
            Session.write_pandas(df_update, "STORE_DATA", auto_create_table=False)
            st.success("Successfully Updated Database!")
    # ----------------------------------------------------------------------
    with t2:
        st.write('<div style="text-align: left; color: yellow;"><h3><em>Displaying Item Prices & Availability</em></h3></div>', unsafe_allow_html=True)

        q_dflog = "select * from logistics"
        cur.execute(q_dflog)
        dflog = cur.fetch_pandas_all()
        dflog = dflog[["PRODUCT_NAME","PRODUCT_ID","CATEGORY","SELL_PRICE","STOCK"]]
        
        s = st.radio("Sort By:",("Name A-Z","Name Z-A", "Category A-Z", "Category Z-A", "Lowest Price","Highest Price"))
        if s == "Name A-Z":
            dflog = dflog.sort_values(by="PRODUCT_NAME", ascending = True)
        elif s == "Name Z-A":
            dflog = dflog.sort_values(by="PRODUCT_NAME", ascending = False)
        elif s == "Category A-Z":
            dflog = dflog.sort_values(by="CATEGORY", ascending = True)
        elif s == "Category Z-A":
            dflog = dflog.sort_values(by="CATEGORY", ascending = False)
        elif s == "Lowest Price":
            dflog = dflog.sort_values(by="SELL_PRICE", ascending = True)
        elif s == "Highest Price":
            dflog = dflog.sort_values(by="SELL_PRICE", ascending = False)
        dflog = dflog.rename(columns = {"SELL_PRICE":"PRICE (€)","STOCK":"AVAILABILITY"}, inplace=True)
        st.dataframe(dflog, width = 1400)
    # ----------------------------------------------------------------------
    # with t3:
    #     st.write('<div style="text-align: left; color: yellow;"><h3><em>Place Your Order here</em></h3></div>', unsafe_allow_html=True)
    #     st.write('<div style="text-align: left; color: yellow;"><h6><em>It will be executed within 1-3 work days, hopefully.</em></h6></div>', unsafe_allow_html=True)

    #     st.write("")
    #     selected_name = st.selectbox("Product Name:", options=dflog["PRODUCT_NAME"].sort_values(ascending = True))

    #     if selected_name != None:
    #         df_info = dflog[dflog["PRODUCT_NAME"] == selected_name]
    #         st.dataframe(df_info, width = 1400)
    #     qty = st.text_input("How many?")
    #     place_order = st.button("Place Order")
    #     if place_order:
    #         # q_order = "select * from logistics where product_name = '"+selected_name+"' limit 1"
    #         # cur.execute(q_order)
    #         # order = cur.fetch_pandas_all()
    #         # order = order[["PRODUCT_NAME","CATEGORY","STOCK"]]
    #         # order["STOCK"] = int(qty)
    #         # order["DATE"] = datetime.today().strftime('%Y-%m-%d')
    #         # order = order[["CATEGORY","DATE","PRODUCT_NAME","STOCK"]]
    #         # Session.write_pandas(df = order, table_name = "PLACE_ORDER", auto_create_table=False)
    #         dflog["AVAILABILITY"][dflog["PRODUCT_NAME"] == selected_name] = dflog["AVAILABILITY"][dflog["PRODUCT_NAME"] == selected_name].tolist()[0] + int(qty)
    #         cur.execute('''CREATE OR REPLACE TABLE logistics (product_name VARCHAR, product_id VARCHAR, category VARCHAR, buy_price FLOAT,
    #                 sell_price FLOAT, stock INTEGER, profit_per_item FLOAT)''')
    #         datalog = dflog.values.tolist()
    #         cur.executemany('''INSERT INTO logistics (product_name, product_id, category, buy_price, sell_price, stock, profit_per_item)
    #                         VALUES (%s, %s, %s, %s, %s, %s, %s)''', datalog)
    #         st.success("Successfully placed your order. Thank you!")

                




 