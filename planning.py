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
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
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
    
    ml_sel = ml[ml["CATEGORY"]=="Accessories"]
    ml_timely = ml_sel.pivot_table(columns="DATE", values="PROFIT", aggfunc="sum", index=["PRODUCT_NAME"]).fillna(0)

    X = ml_timely.drop(columns = "2023-03-01")
    y = ml_timely["2023-03-01"]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.4, random_state = 43)
    num_train = X_train.select_dtypes(np.number)
    num_test = X_test.select_dtypes(np.number)
    scaler = MinMaxScaler().fit(num_train)
    cols = scaler.get_feature_names_out(input_features = num_train.columns)
    num_train_scaled = scaler.transform(num_train)
    num_test_scaled = scaler.transform(num_test)
    num_train_scaled = pd.DataFrame(num_train_scaled, columns = cols)
    num_test_scaled = pd.DataFrame(num_test_scaled, columns = cols)
    X_train_processed = num_train_scaled.copy()
    X_test_processed = num_test_scaled.copy()
    