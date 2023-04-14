def planning():
    import streamlit as st
    import pandas as pd
    import numpy as np
    st.text("planning")
    st.text("overview")
    conn = snowflake.connector.connect(user = "mdimasaac", password = "Qaz1234.", account = "vliobpf-yr09142",
                                    database = "store_it", schema = "store_schema")
    cur = conn.cursor()
    q_df = "select DATE, PRODUCT_NAME, CATEGORY, QUANTITY, PROFIT from store_data"
    cur.execute(q_df)
    df = cur.fetch_pandas_all()
    