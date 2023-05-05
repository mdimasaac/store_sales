def get_ym(a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12):
    y,m = [],[]
    if a01:
        y.append(2019)
        m.append("1")
    if a02:
        y.append(2019)
        m.append("2")
    if a03:
        y.append(2019)
        m.append("3")
    if a04:
        y.append(2019)
        m.append("4")
    if a05:
        y.append(2019)
        m.append("5")
    if a06:
        y.append(2019)
        m.append("6")
    if a07:
        y.append(2019)
        m.append("7")
    if a08:
        y.append(2019)
        m.append("8")
    if a09:
        y.append(2019)
        m.append("9")
    if a10:
        y.append(2019)
        m.append("10")
    if a11:
        y.append(2019)
        m.append("11")
    if a12:
        y.append(2019)
        m.append("12")
    if b01:
        y.append(2020)
        m.append("1")
    if b02:
        y.append(2020)
        m.append("2")
    if b03:
        y.append(2020)
        m.append("3")
    if b04:
        y.append(2020)
        m.append("4")
    if b05:
        y.append(2020)
        m.append("5")
    if b06:
        y.append(2020)
        m.append("6")
    if b07:
        y.append(2020)
        m.append("7")
    if b08:
        y.append(2020)
        m.append("8")
    if b09:
        y.append(2020)
        m.append("9")
    if b10:
        y.append(2020)
        m.append("10")
    if b11:
        y.append(2020)
        m.append("11")
    if b12:
        y.append(2020)
        m.append("12")
    if c01:
        y.append(2021)
        m.append("1")
    if c02:
        y.append(2021)
        m.append("2")
    if c03:
        y.append(2021)
        m.append("3")
    if c04:
        y.append(2021)
        m.append("4")
    if c05:
        y.append(2021)
        m.append("5")
    if c06:
        y.append(2021)
        m.append("6")
    if c07:
        y.append(2021)
        m.append("7")
    if c08:
        y.append(2021)
        m.append("8")
    if c09:
        y.append(2021)
        m.append("9")
    if c10:
        y.append(2021)
        m.append("10")
    if c11:
        y.append(2021)
        m.append("11")
    if c12:
        y.append(2021)
        m.append("12")
    if d01:
        y.append(2022)
        m.append("1")
    if d02:
        y.append(2022)
        m.append("2")
    if d03:
        y.append(2022)
        m.append("3")
    if d04:
        y.append(2022)
        m.append("4")
    if d05:
        y.append(2022)
        m.append("5")
    if d06:
        y.append(2022)
        m.append("6")
    if d07:
        y.append(2022)
        m.append("7")
    if d08:
        y.append(2022)
        m.append("8")
    if d09:
        y.append(2022)
        m.append("9")
    if d10:
        y.append(2022)
        m.append("10")
    if d11:
        y.append(2022)
        m.append("11")
    if d12:
        y.append(2022)
        m.append("12")
        M.append("Dec")
    if e01:
        y.append(2023)
        m.append("1")
    if e02:
        y.append(2023)
        m.append("2")
    if e03:
        y.append(2023)
        m.append("3")
    if e04:
        y.append(2023)
        m.append("4")
    if e05:
        y.append(2023)
        m.append("5")
    if e06:
        y.append(2023)
        m.append("6")
    if e07:
        y.append(2023)
        m.append("7")
    if e08:
        y.append(2023)
        m.append("8")
    if e09:
        y.append(2023)
        m.append("9")
    if e10:
        y.append(2023)
        m.append("10")
    if e11:
        y.append(2023)
        m.append("11")
    if e12:
        y.append(2023)
        m.append("12")
    return y,m

def show_checkboxes():
    import streamlit as st
    cola,colb,colc,cold,cole = st.columns(5)
    with cola:
        st.write("2019")
        cola1,cola2,ca3 = st.columns([2,2,1])
        with cola1:
            a01 = st.checkbox("Jan", key="a01")
            a02 = st.checkbox("Feb", key="a02")
            a03 = st.checkbox("Mar", key="a03")
            a04 = st.checkbox("Apr", key="a04")
            a05 = st.checkbox("May", key="a05")
            a06 = st.checkbox("Jun", key="a06")
        with cola2:
            a07 = st.checkbox("Jul", key="a07")
            a08 = st.checkbox("Aug", key="a08")
            a09 = st.checkbox("Sep", key="a09")
            a10 = st.checkbox("Oct", key="a10")
            a11 = st.checkbox("Nov", key="a11")
            a12 = st.checkbox("Dec", key="a12")
        with ca3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with colb:    
        st.write("2020")
        colb1,colb2,cb3 = st.columns([2,2,1])
        with colb1:
            b01 = st.checkbox("Jan", key="b01")
            b02 = st.checkbox("Feb", key="b02")
            b03 = st.checkbox("Mar", key="b03")
            b04 = st.checkbox("Apr", key="b04")
            b05 = st.checkbox("May", key="b05")
            b06 = st.checkbox("Jun", key="b06")
        with colb2:
            b07 = st.checkbox("Jul", key="b07")
            b08 = st.checkbox("Aug", key="b08")
            b09 = st.checkbox("Sep", key="b09")
            b10 = st.checkbox("Oct", key="b10")
            b11 = st.checkbox("Nov", key="b11")
            b12 = st.checkbox("Dec", key="b12")
        with cb3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with colc:
        st.write("2021")
        colc1,colc2,cc3 = st.columns([2,2,1])
        with colc1:
            c01 = st.checkbox("Jan", key="c01")
            c02 = st.checkbox("Feb", key="c02")
            c03 = st.checkbox("Mar", key="c03")
            c04 = st.checkbox("Apr", key="c04")
            c05 = st.checkbox("May", key="c05")
            c06 = st.checkbox("Jun", key="c06")
        with colc2:
            c07 = st.checkbox("Jul", key="c07")
            c08 = st.checkbox("Aug", key="c08")
            c09 = st.checkbox("Sep", key="c09")
            c10 = st.checkbox("Oct", key="c10")
            c11 = st.checkbox("Nov", key="c11")
            c12 = st.checkbox("Dec", key="c12")
        with cc3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with cold:
        st.write("2022")
        cold1,cold2,cd3 = st.columns([2,2,1])
        with cold1:
            d01 = st.checkbox("Jan", key="d01")
            d02 = st.checkbox("Feb", key="d02")
            d03 = st.checkbox("Mar", key="d03")
            d04 = st.checkbox("Apr", key="d04")
            d05 = st.checkbox("May", key="d05")
            d06 = st.checkbox("Jun", key="d06")
        with cold2:
            d07 = st.checkbox("Jul", key="d07")
            d08 = st.checkbox("Aug", key="d08")
            d09 = st.checkbox("Sep", key="d09")
            d10 = st.checkbox("Oct", key="d10")
            d11 = st.checkbox("Nov", key="d11")
            d12 = st.checkbox("Dec", key="d12")
        with cd3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with cole:
        st.write("2023")
        cole1,cole2,ce3 = st.columns([2,2,1])
        with cole1:
            e01 = st.checkbox("Jan", key="e01")
            e02 = st.checkbox("Feb", key="e02")
            e03 = st.checkbox("Mar", key="e03")
            e04 = st.checkbox("Apr", key="e04")
            e05 = st.checkbox("May", key="e05")
            e06 = st.checkbox("Jun", key="e06")
        with cole2:
            e07 = st.checkbox("Jul", key="e07")
            e08 = st.checkbox("Aug", key="e08")
            e09 = st.checkbox("May", key="e09")
            e10 = st.checkbox("Jun", key="e10")
            e11 = st.checkbox("Jul", key="e11")
            e12 = st.checkbox("Aug", key="e12")
        with ce3:
            st.write(" ")
        st.write("_________")
    y,m = get_ym(a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12)    
    return y,m

def show_checkboxes2():
    import streamlit as st
    cola,colb,colc,cold,cole = st.columns(5)
    with cola:
        st.write("2019")
        cola1,cola2,ca3 = st.columns([2,2,1])
        with cola1:
            a01 = st.checkbox("Jan", key="aa01")
            a02 = st.checkbox("Feb", key="aa02")
            a03 = st.checkbox("Mar", key="aa03")
            a04 = st.checkbox("Apr", key="aa04")
            a05 = st.checkbox("May", key="aa05")
            a06 = st.checkbox("Jun", key="aa06")
        with cola2:
            a07 = st.checkbox("Jul", key="aa07")
            a08 = st.checkbox("Aug", key="aa08")
            a09 = st.checkbox("Sep", key="aa09")
            a10 = st.checkbox("Oct", key="aa10")
            a11 = st.checkbox("Nov", key="aa11")
            a12 = st.checkbox("Dec", key="aa12")
        with ca3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with colb:    
        st.write("2020")
        colb1,colb2,cb3 = st.columns([2,2,1])
        with colb1:
            b01 = st.checkbox("Jan", key="bb01")
            b02 = st.checkbox("Feb", key="bb02")
            b03 = st.checkbox("Mar", key="bb03")
            b04 = st.checkbox("Apr", key="bb04")
            b05 = st.checkbox("May", key="bb05")
            b06 = st.checkbox("Jun", key="bb06")
        with colb2:
            b07 = st.checkbox("Jul", key="bb07")
            b08 = st.checkbox("Aug", key="bb08")
            b09 = st.checkbox("Sep", key="bb09")
            b10 = st.checkbox("Oct", key="bb10")
            b11 = st.checkbox("Nov", key="bb11")
            b12 = st.checkbox("Dec", key="bb12")
        with cb3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with colc:
        st.write("2021")
        colc1,colc2,cc3 = st.columns([2,2,1])
        with colc1:
            c01 = st.checkbox("Jan", key="cc01")
            c02 = st.checkbox("Feb", key="cc02")
            c03 = st.checkbox("Mar", key="cc03")
            c04 = st.checkbox("Apr", key="cc04")
            c05 = st.checkbox("May", key="cc05")
            c06 = st.checkbox("Jun", key="cc06")
        with colc2:
            c07 = st.checkbox("Jul", key="cc07")
            c08 = st.checkbox("Aug", key="cc08")
            c09 = st.checkbox("Sep", key="cc09")
            c10 = st.checkbox("Oct", key="cc10")
            c11 = st.checkbox("Nov", key="cc11")
            c12 = st.checkbox("Dec", key="cc12")
        with cc3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with cold:
        st.write("2022")
        cold1,cold2,cd3 = st.columns([2,2,1])
        with cold1:
            d01 = st.checkbox("Jan", key="dd01")
            d02 = st.checkbox("Feb", key="dd02")
            d03 = st.checkbox("Mar", key="dd03")
            d04 = st.checkbox("Apr", key="dd04")
            d05 = st.checkbox("May", key="dd05")
            d06 = st.checkbox("Jun", key="dd06")
        with cold2:
            d07 = st.checkbox("Jul", key="dd07")
            d08 = st.checkbox("Aug", key="dd08")
            d09 = st.checkbox("Sep", key="dd09")
            d10 = st.checkbox("Oct", key="dd10")
            d11 = st.checkbox("Nov", key="dd11")
            d12 = st.checkbox("Dec", key="dd12")
        with cd3:
            st.write(" ")
        st.write("_________")
    # --------------------------------------------------
    with cole:
        st.write("2023")
        cole1,cole2,ce3 = st.columns([2,2,1])
        with cole1:
            e01 = st.checkbox("Jan", key="ee01")
            e02 = st.checkbox("Feb", key="ee02")
            e03 = st.checkbox("Mar", key="ee03")
            e04 = st.checkbox("Apr", key="ee04")
            e05 = st.checkbox("May", key="ee05")
            e06 = st.checkbox("Jun", key="ee06")
        with cole2:
            e07 = st.checkbox("Jul", key="ee07")
            e08 = st.checkbox("Aug", key="ee08")
            e09 = st.checkbox("May", key="ee09")
            e10 = st.checkbox("Jun", key="ee10")
            e11 = st.checkbox("Jul", key="ee11")
            e12 = st.checkbox("Aug", key="ee12")
        with ce3:
            st.write(" ")
        st.write("_________")
    y,m = get_ym(a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,b01,b02,b03,b04,b05,b06,b07,b08,b09,b10,b11,b12,c01,c02,c03,c04,c05,c06,c07,c08,c09,c10,c11,c12,d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12,e01,e02,e03,e04,e05,e06,e07,e08,e09,e10,e11,e12)    
    return y,m

def store_management():
    import streamlit as st
    import pandas as pd
    import snowflake.connector
    from datetime import datetime
    from snowflake.snowpark import Session
    conn = snowflake.connector.connect(user = "mdimasaac", password = "Snowflake123", account = "vliobpf-yr09142",
                                    database = "store_it", schema = "store_schema")
    cur = conn.cursor()
    t1,t2,t3 = st.tabs(["Transactions","Profits","Edit Price"])
    # --------------------------------------------------
    with t1:
        # no changes to snowflake data. just fetching
        qdf = "select * from store_data"
        cur.execute(qdf)
        df = cur.fetch_pandas_all()
        st.write('<div style="text-align: left; color: yellow;"><h3><em>Display Most Actual In-Store Transactions</em></h3></div>', unsafe_allow_html=True)
        n = st.radio("Show last [...] transactions",("10","25","50","100","200"))
        show = df.sort_values(by="DATE", ascending = False).head(int(n))
        show["YEAR"] = show["YEAR"].astype(str).str.replace(",","")
        st.write('<div style="text-align: left;"><h6><em>Note that the data is displayed in reversed order.</em></h6></div>', unsafe_allow_html=True)
        show = show[["DATE","PRODUCT_NAME","CATEGORY","QUANTITY","SALES","PROFIT"]]
        st.dataframe(show, width = 1400)
        st.write("_________")
        show2 = show.head(0)
        st.write('<div style="text-align: left;"><h5><em>Display the data on month(s)</em></h5></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left; color: yellow;"><h6>(Hint: click on the month(s) to display all transactions in chosen month)</h6></div>', unsafe_allow_html=True)

        st.write(" ")
        y,m = show_checkboxes()
        # --------------------------------------------------
        df_sorted = df.sort_values(by="DATE", ascending = False)
        for i in range(len(y)):
            add2 = df_sorted[(df_sorted["YEAR"]==(y[i])) & (df_sorted["MONTH"]==m[i])]
            show2 = pd.concat([show2,add2], axis = 0)
        if len(y) != 0:
            show2["YEAR"] = show2["YEAR"].astype(str).str.replace(",","")
            show2 = show2[["DATE","PRODUCT_NAME","CATEGORY","QUANTITY","SALES","PROFIT"]]
            st.dataframe(show2, width = 1400)
    # --------------------------------------------------
    with t2:
        # no changes to snowflake data. just fetching
        st.write('<div style="text-align: left; color: yellow;"><h3><em>Profit Monitor</em></h3></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left; color: yellow;"><h6>Showing monthly profit by each category</h6></div>', unsafe_allow_html=True)
        st.write('<div style="text-align: left; color: yellow;"><h6>(Hint: click on the month(s) to display the profit)</h6></div>', unsafe_allow_html=True)

        show3 = show.head(0)
        y3,m3 = show_checkboxes2()
        for i in range(len(y3)):
            add3 = df_sorted[(df_sorted["YEAR"]==(y3[i])) & (df_sorted["MONTH"]==m3[i])]
            show3 = pd.concat([show3,add3], axis = 0)

        show3['DATE'] = pd.to_datetime(show3['DATE']).dt.strftime('%b %Y')
        show3 = show3.sort_values(by="DATE")
        show3['DATE'] = pd.to_datetime(show3['DATE'], format='%b %Y')
        show3 = show3.reset_index(drop=True)
        pt = show3.pivot_table(columns = "CATEGORY", values = "PROFIT", aggfunc = "sum", index = "DATE")
        if len(y3) != 0:
            st.dataframe(pt, width = 1400)
    # --------------------------------------------------
    with t3:
        # apply changes to snowflake data
        st.write('<div style="text-align: left; color: yellow;"><h3><em>Change Product Price</em></h3></div>', unsafe_allow_html=True)
        q_dflog = "select * from logistics"
        cur.execute(q_dflog)
        dflog = cur.fetch_pandas_all()
        dflog_info = dflog[["PRODUCT_NAME","PRODUCT_ID","CATEGORY","SELL_PRICE","STOCK"]]
        selected_name = st.selectbox("Product Name:", options=dflog["PRODUCT_NAME"].sort_values(ascending = True))
        if selected_name != None:
            df_info = dflog_info[dflog_info["PRODUCT_NAME"] == selected_name]
            st.dataframe(df_info, width = 1400)
        c1,c2,c3 = st.columns([1,1,2])
        with c1:
            new_price = st.text_input("New Price:")
        with c2:
            st.write(" ")
            st.write(" ")
            change = st.button("Set New Price")
        with c3:
            st.write(" ")
        see = False
        if change:
            dflog["SELL_PRICE"][dflog["PRODUCT_NAME"] == selected_name] = new_price
            cur.execute('''CREATE OR REPLACE TABLE logistics (product_name VARCHAR, product_id VARCHAR, category VARCHAR, buy_price FLOAT,
                    sell_price FLOAT, stock INTEGER, profit_per_item FLOAT)''')
            datalog = dflog.values.tolist()
            cur.executemany('''INSERT INTO logistics (product_name, product_id, category, buy_price, sell_price, stock, profit_per_item)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)''', datalog)
            
            st.success("Price was updated.")
            see = st.button("Fetch Price from Database")
        if see:
            q_dflog = "select * from logistics"
            cur.execute(q_dflog)
    # with t4:
    #     st.write('<div style="text-align: left; color: yellow;"><h3><em>Manage Order</em></h3></div>', unsafe_allow_html=True)
    #     q_order = "select * from place_order"
    #     cur.execute(q_order)
    #     order = cur.fetch_pandas_all()
    #     st.write('<div style="text-align: left; color: yellow;"><h5><em>Displaying placed order.</em></h5></div>', unsafe_allow_html=True)
    #     st.dataframe(order, width = 1400)

    #     q_dflog = "select * from logistics"
    #     cur.execute(q_dflog)
    #     dflog = cur.fetch_pandas_all()
    #     dflog_info = dflog[["PRODUCT_NAME","PRODUCT_ID","CATEGORY","SELL_PRICE","STOCK"]]
    #     selected_name2 = st.selectbox("Product Name:", options=dflog["PRODUCT_NAME"].sort_values(ascending = True), key = "name2")
    #     if selected_name2 != None:
    #         df_info = dflog_info[dflog_info["PRODUCT_NAME"] == selected_name2]
    #         st.dataframe(df_info, width = 1400)
    #     c1,c2,c3 = st.columns([1,1,2])
    #     with c1:
    #         new_stock = st.text_input("Add how many items to stock:")
    #     with c2:
    #         st.write(" ")
    #         st.write(" ")
    #         restock = st.button("Restock")
    #     with c3:
    #         st.write(" ")
        
    #     see2 = False
    #     if restock:
    #         dflog["STOCK"][dflog["PRODUCT_NAME"] == selected_name2] = new_stock
    #         cur.execute('''CREATE OR REPLACE TABLE logistics (product_name VARCHAR, product_id VARCHAR, category VARCHAR, buy_price FLOAT,
    #                 sell_price FLOAT, stock INTEGER, profit_per_item FLOAT)''')
    #         datalog = dflog.values.tolist()
    #         cur.executemany('''INSERT INTO logistics (product_name, product_id, category, buy_price, sell_price, stock, profit_per_item)
    #                         VALUES (%s, %s, %s, %s, %s, %s, %s)''', datalog)
            
    #         st.success("Price was updated.")
    #         see2 = st.button("Fetch Data")
    #     if see2:
    #         q_dflog = "select * from logistics"
    #         cur.execute(q_dflog)

        










