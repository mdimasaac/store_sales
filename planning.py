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
    import snowflake.connector
    from datetime import datetime
    from snowflake.snowpark import Session
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
    
    c1, c2 = st.columns(2)
    with c1:
        options_left = ["Linear Regression","MLP","K-Neighbors","Decision Tree","Random Forest"]
        ml_left = st.radio(label='Choose Machine Learning Model:', options=options_left,
                            key = 'ml_left'
                            )
        st.write("_________")

        if ml_left == "Linear Regression":
            model_left = LinearRegression()
            st.subheader("Play Around with the Parameters!")
            col11,col12 = st.columns(2)
            with col11:
                fint_left = st.radio("fit_intercept:",("True","False"), key = "fint_left")
                if fint_left == "True":
                    fint_left = True
                else:
                    fint_left = False
            with col12:
                pos_left = st.radio("positive:",("True","False"), key = "pos_left")
                if pos_left == "True":
                    pos_left = True
                else:
                    pos_left = False
            st.subheader("Or Optimize Parameter")
            opt_left = st.checkbox("Optimize", key = "opt1_left")
            if opt_left:
                lfint_left = [True, False]
                lpos_left = [True, False]
                grid_left = {"fit_intercept":lfint_left,"positive":lpos_left}
                grid_search_left = GridSearchCV(estimator = model_left, param_grid = grid_left, cv = 5)
                grid_search_left.fit(X_test_processed, y_test)
                fint_left = grid_search_left.best_params_["fit_intercept"]
                pos_left = grid_search_left.best_params_["positive"]
            regr_left = LinearRegression(fit_intercept=fint_left, positive=pos_left)

        elif ml_left == "MLP":
            model_left = MLPRegressor()
            st.subheader("Play Around with the Parameters!")
            hlsize_left = st.slider("hidden_layer_sizes:", 50,300,50,50, key = "hlsize_left")
            maxiter_left = st.slider("max_iter:", 200,700,200,100, key = "maxiter_left")
            col11,col12 = st.columns(2)
            with col11:
                solver_left = st.radio("solver:", ("lbfgs","sgd","adam"), key = "solver_left")
            with col12:
                rate_left = st.radio("learning_rate:",("constant","invscaling","adaptive"), key = "rate_left")
            st.subheader("Or Optimize Parameter")
            opt_left = st.checkbox("Optimize", key = "opt2_left")
            if opt_left:
                lhlsize_left = list(range(200,301,100))
                lmaxiter_left = list(range(600,701,100))
                lsolver_left = ["lbfgs","sgd","adam"]
                lrate_left = ["constant","invscaling","adaptive"]
                grid_left = {"hidden_layer_sizes":lhlsize_left, "max_iter":lmaxiter_left,
                            "solver":lsolver_left, "learning_rate":lrate_left}
                grid_search_left = GridSearchCV(estimator = model_left, param_grid = grid_left, cv = 5)
                grid_search_left.fit(X_test_processed, y_test)
                hlsize_left = grid_search_left.best_params_["hidden_layer_sizes"]
                maxiter_left = grid_search_left.best_params_["max_iter"]
                solver_left = grid_search_left.best_params_["solver"]
                rate_left = grid_search_left.best_params_["learning_rate"]
            regr_left = MLPRegressor(hidden_layer_sizes = hlsize_left, max_iter = maxiter_left,
                                    solver = solver_left, learning_rate = rate_left)
    
        elif ml_left == "K-Neighbors":
            model_left = KNeighborsRegressor()
            st.subheader("Play Around with the Parameters!")
            n_left = st.slider("n_neighbors:", 3,9,3,1, key = "n_left")
            weight_left = st.radio("weight:", ("uniform","distance"), key = "weight_left")
            alg_left = "auto"
            st.subheader("Or Optimize Parameter")
            opt_left = st.checkbox("Optimize", key = "opt3_left")
            if opt_left:
                ln_left = list(range(3,10,1))
                lweight_left = ["uniform","distance"]
                lalg_left = ["auto"]
                grid_left = {"n_neighbors":ln_left, "weights":lweight_left, "algorithm":lalg_left}
                grid_search_left = GridSearchCV(estimator = model_left, param_grid = grid_left, cv = 5)
                grid_search_left.fit(X_test_processed, y_test)
                n_left = grid_search_left.best_params_["n_neighbors"]
                weight_left = grid_search_left.best_params_["weights"]
                alg_left = "auto"
            regr_left = KNeighborsRegressor(n_neighbors = n_left, weights = weight_left, algorithm = alg_left)
        
        elif ml_left == "Decision Tree":
            model_left = DecisionTreeRegressor()
            st.subheader("Play Around with the Parameters!")
            minsplit_left = st.slider("min_samples_split:",2,10,2,1, key = "split1_left")
            minleaf_left = st.slider("min_samples_leaf:", 2,10,2,1, key = "leaf1_left")
            col11,col12,col13 = st.columns([1,1,2])
            with col11:
                depth_left = st.radio("max_depth:", (3,4,5,6,7,None), key = "depth1_left")
            with col12:
                feat_left = st.radio("max_features:", (2,3,4,None), key = "feat1_left")
            with col13:
                crit_left = st.radio("criterion:",('squared_error','absolute_error'), key = "crit1_left")
            st.subheader("Or Optimize Parameter")
            opt_left = st.checkbox("Optimize", key = "opt4_left")
            if opt_left:
                lminsplit_left = list(range(4,8))
                lminleaf_left = list(range(4,8))
                ldepth_left = [6,7,None]
                lfeat_left = [3,4,None]
                lcrit_left = ['squared_error','absolute_error']
                grid_left = {"min_samples_split":lminsplit_left,"min_samples_leaf":lminleaf_left,
                            "max_depth":ldepth_left,"max_features":lfeat_left,"criterion":lcrit_left}
                with st.spinner("Running Algorithm.."):
                    grid_search_left = GridSearchCV(estimator = model_left, param_grid = grid_left, cv = 5)
                grid_search_left.fit(X_test_processed, y_test)
                minsplit_left = grid_search_left.best_params_["min_samples_split"]
                minleaf_left = grid_search_left.best_params_["min_samples_leaf"]
                depth_left = grid_search_left.best_params_["max_depth"]
                feat_left = grid_search_left.best_params_["max_features"]
                crit_left = grid_search_left.best_params_["criterion"]
            regr_left = DecisionTreeRegressor(min_samples_split = minsplit_left,
                        min_samples_leaf = minleaf_left, max_depth = depth_left, 
                        max_features = feat_left, criterion = crit_left)
        
        elif ml_left == "Random Forest":
            model_left = RandomForestRegressor()
            st.subheader("Play Around with the Parameters!")
            minsplit_left = st.slider("min_samples_split:",2,10,2,1, key = "split2_left")
            minleaf_left = st.slider("min_samples_leaf:", 2,10,2,1, key = "leaf2_left")
            col11,col12,col13 = st.columns([1,1,2])
            with col11:
                depth_left = st.radio("max_depth:", (3,4,5,6,7,None), key = "depth2_left")
            with col12:
                feat_left = st.radio("max_features:", (2,3,4,None), key = "feat2_left")
            with col13:
                crit_left = st.radio("criterion:",('squared_error','absolute_error'), key = "crit2_left")
            st.subheader("Or Optimize Parameter")
            opt_left = st.checkbox("Optimize", key = "opt5_left")
            if opt_left:
                lminsplit_left = list(range(4,8))
                lminleaf_left = list(range(4,8))
                ldepth_left = [6,7,None]
                lfeat_left = [3,4,None]
                lcrit_left = ['squared_error','absolute_error']
                grid_left = {"min_samples_split":lminsplit_left,"min_samples_leaf":lminleaf_left,
                            "max_depth":ldepth_left,"max_features":lfeat_left,"criterion":lcrit_left}
                with st.spinner("Running Algorithm.."):
                    grid_search_left = GridSearchCV(estimator = model_left, param_grid = grid_left, cv = 5)
                grid_search_left.fit(X_test_processed, y_test)
                minsplit_left = grid_search_left.best_params_["min_samples_split"]
                minleaf_left = grid_search_left.best_params_["min_samples_leaf"]
                depth_left = grid_search_left.best_params_["max_depth"]
                feat_left = grid_search_left.best_params_["max_features"]
                crit_left = grid_search_left.best_params_["criterion"]
            regr_left = RandomForestRegressor(min_samples_split = minsplit_left,
                        min_samples_leaf = minleaf_left, max_depth = depth_left, 
                        max_features = feat_left, criterion = crit_left)

    with c2:
        lcat = []
        listcat = df["CATEGORY"].unique().tolist()
        st.radio("Choose a Product Category", (listcat[0],listcat[1],listcat[2],listcat[3],listcat[4],listcat[5],listcat[6],
                    listcat[7],listcat[8],listcat[9],listcat[10],listcat[11],listcat[12],listcat[13],listcat[14],listcat[15],listcat[16],listcat[16]))
        
 


            










    # ml_sel = df[df["CATEGORY"]==cat]
    # ml_timely = ml_sel.pivot_table(columns="DATE", values="PROFIT", aggfunc="sum", index=["PRODUCT_NAME"]).fillna(0)

    # X = ml_timely.drop(columns = "2023-03-01")
    # y = ml_timely["2023-03-01"]
    # X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.4, random_state = 43)
    # num_train = X_train.select_dtypes(np.number)
    # num_test = X_test.select_dtypes(np.number)
    # scaler = MinMaxScaler().fit(num_train)
    # cols = scaler.get_feature_names_out(input_features = num_train.columns)
    # num_train_scaled = scaler.transform(num_train)
    # num_test_scaled = scaler.transform(num_test)
    # num_train_scaled = pd.DataFrame(num_train_scaled, columns = cols)
    # num_test_scaled = pd.DataFrame(num_test_scaled, columns = cols)
    # X_train_processed = num_train_scaled.copy()
    # X_test_processed = num_test_scaled.copy()
    