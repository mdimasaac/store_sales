def planning():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    from sklearn.model_selection import GridSearchCV
    from sklearn.linear_model import LinearRegression
    from sklearn.neural_network import MLPRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import cross_val_score
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)
    from warnings import simplefilter
    from sklearn.exceptions import ConvergenceWarning
    simplefilter("ignore", category=ConvergenceWarning)
    
    st.text("planning")
    st.text("overview")
    conn = snowflake.connector.connect(user = "mdimasaac", password = "Qaz1234.", account = "vliobpf-yr09142",
                                    database = "store_it", schema = "store_schema")
    cur = conn.cursor()
    q_df = "select DATE, PRODUCT_NAME, CATEGORY, QUANTITY, PROFIT from store_data"
    cur.execute(q_df)
    df = cur.fetch_pandas_all()

    df['DATE'] = pd.to_datetime(df['DATE']).dt.strftime('%b %Y')
    df = df.sort_values(by="DATE")
    df['DATE'] = pd.to_datetime(df['DATE'], format='%b %Y')
    df = df.reset_index(drop=True)
    