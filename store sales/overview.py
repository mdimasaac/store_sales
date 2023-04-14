def overview():
    import streamlit as st
    import pandas as pd
    import snowflake.connector
    import plotly.express as px
    import plotly.graph_objects as go
    from streamlit_plotly_events import plotly_events

    st.text("overview")
    conn = snowflake.connector.connect(user = "mdimasaac", password = "Qaz1234.", account = "vliobpf-yr09142",
                                    database = "store_it", schema = "store_schema")
    cur = conn.cursor()
    q_df = "select * from store_data"
    cur.execute(q_df)
    df = cur.fetch_pandas_all()
    data,y,m,M = [],[],[],[]

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
        if a01:
            y.append(2019)
            m.append("1")
            M.append("Jan")
        if a02:
            y.append(2019)
            m.append("2")
            M.append("Feb")
        if a03:
            y.append(2019)
            m.append("3")
            M.append("Mar")
        if a04:
            y.append(2019)
            m.append("4")
            M.append("Apr")
        if a05:
            y.append(2019)
            m.append("5")
            M.append("May")
        if a06:
            y.append(2019)
            m.append("6")
            M.append("Jun")
        if a07:
            y.append(2019)
            m.append("7")
            M.append("Jul")
        if a08:
            y.append(2019)
            m.append("8")
            M.append("Aug")
        if a09:
            y.append(2019)
            m.append("9")
            M.append("Sep")
        if a10:
            y.append(2019)
            m.append("10")
            M.append("Oct")
        if a11:
            y.append(2019)
            m.append("11")
            M.append("Nov")
        if a12:
            y.append(2019)
            m.append("12")
            M.append("Dec")
        if b01:
            y.append(2020)
            m.append("1")
            M.append("Jan")
        if b02:
            y.append(2020)
            m.append("2")
            M.append("Feb")
        if b03:
            y.append(2020)
            m.append("3")
            M.append("Mar")
        if b04:
            y.append(2020)
            m.append("4")
            M.append("Apr")
        if b05:
            y.append(2020)
            m.append("5")
            M.append("May")
        if b06:
            y.append(2020)
            m.append("6")
            M.append("Jun")
        if b07:
            y.append(2020)
            m.append("7")
            M.append("Jul")
        if b08:
            y.append(2020)
            m.append("8")
            M.append("Aug")
        if b09:
            y.append(2020)
            m.append("9")
            M.append("Sep")
        if b10:
            y.append(2020)
            m.append("10")
            M.append("Oct")
        if b11:
            y.append(2020)
            m.append("11")
            M.append("Nov")
        if b12:
            y.append(2020)
            m.append("12")
            M.append("Dec")
        if c01:
            y.append(2021)
            m.append("1")
            M.append("Jan")
        if c02:
            y.append(2021)
            m.append("2")
            M.append("Feb")
        if c03:
            y.append(2021)
            m.append("3")
            M.append("Mar")
        if c04:
            y.append(2021)
            m.append("4")
            M.append("Apr")
        if c05:
            y.append(2021)
            m.append("5")
            M.append("May")
        if c06:
            y.append(2021)
            m.append("6")
            M.append("Jun")
        if c07:
            y.append(2021)
            m.append("7")
            M.append("Jul")
        if c08:
            y.append(2021)
            m.append("8")
            M.append("Aug")
        if c09:
            y.append(2021)
            m.append("9")
            M.append("Sep")
        if c10:
            y.append(2021)
            m.append("10")
            M.append("Oct")
        if c11:
            y.append(2021)
            m.append("11")
            M.append("Nov")
        if c12:
            y.append(2021)
            m.append("12")
            M.append("Dec")
        if d01:
            y.append(2022)
            m.append("1")
            M.append("Jan")
        if d02:
            y.append(2022)
            m.append("2")
            M.append("Feb")
        if d03:
            y.append(2022)
            m.append("3")
            M.append("Mar")
        if d04:
            y.append(2022)
            m.append("4")
            M.append("Apr")
        if d05:
            y.append(2022)
            m.append("5")
            M.append("May")
        if d06:
            y.append(2022)
            m.append("6")
            M.append("Jun")
        if d07:
            y.append(2022)
            m.append("7")
            M.append("Jul")
        if d08:
            y.append(2022)
            m.append("8")
            M.append("Aug")
        if d09:
            y.append(2022)
            m.append("9")
            M.append("Sep")
        if d10:
            y.append(2022)
            m.append("10")
            M.append("Oct")
        if d11:
            y.append(2022)
            m.append("11")
            M.append("Nov")
        if d12:
            y.append(2022)
            m.append("12")
            M.append("Dec")
        if e01:
            y.append(2023)
            m.append("1")
            M.append("Jan")
        if e02:
            y.append(2023)
            m.append("2")
            M.append("Feb")
        if e03:
            y.append(2023)
            m.append("3")
            M.append("Mar")
        if e04:
            y.append(2023)
            m.append("4")
            M.append("Apr")
        if e05:
            y.append(2023)
            m.append("5")
            M.append("May")
        if e06:
            y.append(2023)
            m.append("6")
            M.append("Jun")
        if e07:
            y.append(2023)
            m.append("7")
            M.append("Jul")
        if e08:
            y.append(2023)
            m.append("8")
            M.append("Aug")
        if e09:
            y.append(2023)
            m.append("9")
            M.append("Sep")
        if e10:
            y.append(2023)
            m.append("10")
            M.append("Oct")
        if e11:
            y.append(2023)
            m.append("11")
            M.append("Nov")
        if e12:
            y.append(2023)
            m.append("12")
            M.append("Dec")
        
    x = df["CATEGORY"].sort_values().unique().tolist()
    for i in range(len(y)):
        data.append(go.Bar(name=M[i]+" "+str(y[i]), x=x,
             y=df[["CATEGORY","PROFIT"]][(df["MONTH"] == m[i]) & (df["YEAR"] == y[i])].groupby(["CATEGORY"]).sum()["PROFIT"]))
    
    fig = go.Figure(data=data)
    fig.update_layout(barmode='group', template="plotly_dark", autosize=True)
    selected = plotly_events(fig)    

    if len(selected) != 0:
        colf1,colf2 = st.columns([2,1])
        selected2 = []
        with colf1:
            try:
                cat = selected[0][list(selected[0].keys())[0]]
                sel = (selected[0][list(selected[0].keys())[2]])
            except:
                pass
            fil = df[(df["CATEGORY"]==cat) & (df["YEAR"]==y[sel]) & (df["MONTH"]==m[sel])].sort_values(by="PROFIT", ascending = False)
            top = fil.groupby(["PRODUCT_NAME"]).sum().sort_values(by="PROFIT", ascending = False).head(10).index.values.tolist()
            prod = []
            for i in fil["PRODUCT_NAME"]:
                if (i in top):
                    prod.append(i)
                else:
                    prod.append("Others")
            fil["PRODUCT_NAME"] = prod
            filtered = fil.groupby(["PRODUCT_NAME"]).sum().sort_values(by="PROFIT", ascending = False)
            labels = filtered.index.values.tolist()
            pull = []
            for i in range(len(labels)):
                pull.append(0.1)
            fig2 = go.Figure(go.Pie(
                                labels = labels,
                                values = filtered.PROFIT.values.round(2).tolist(),hovertemplate = "%{label}<br>%{percent} <extra></extra>",
                                hole=.7,
                                marker_line_color='white',
                                marker_line_width=1.25,
                                pull= pull,
                                textinfo="label+percent"
                            ))
            fig2.update_layout(
                        autosize=True,  # Automatically adjust size to fit entire layout
                        margin=dict(l=0, r=0, t=0, b=0),)  # Remove margin around chart
            fig2.update_layout(showlegend=False, template="plotly_dark")
            fig2.update_layout(
            font=dict(
            size=16,))

            selected2 = plotly_events(fig2)
            
        with colf2:
            if len(selected2) != 0:
                ind = selected2[0][list(selected2[0].keys())[1]]
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.text(" ")
                st.write("_________") 
                st.text("Showing Details for Clicked Bar Chart:")
                st.text(cat+" in "+M[sel]+" "+str(y[sel]))
                cf1,cf2 = st.columns(2)
                with cf1:
                    st.text("Num. of Transactions")
                    st.text(fil.shape[0])
                with cf2:
                    st.text("Total Items Sold")
                    st.text(fil["QUANTITY"].sum())
                st.write("_________")
                st.text("Showing Details for Clicked Donut Area:")
                st.text(labels[ind])
                cf3,cf4 = st.columns(2)
                with cf3:
                    st.text("Profit per Item")
                    st.text(filtered["PROFIT_PER_ITEM"][filtered.index.values == labels[ind]].values.tolist()[0])
                with cf4:
                    st.text("Sum Profit by This Item")
                    st.text(fil["PROFIT"][fil["PRODUCT_NAME"] == labels[ind]].sum())
                st.write("_________") 

        if len(selected2) != 0:
            ind = selected2[0][list(selected2[0].keys())[1]]
            st.text("Line Chart for " + labels[ind])
            dfline = df[["DATE","PROFIT"]][df["PRODUCT_NAME"] == labels[ind]].sort_values(by="DATE", ascending = True)
            fig3 = px.line(dfline, x="DATE", y="PROFIT", title=labels[ind])
            fig3.update_layout(template = "plotly_dark",autosize = True)
            st.plotly_chart(fig3, use_container_width=True)


            # st.line_chart(dfline, use_container_width=True)


        

