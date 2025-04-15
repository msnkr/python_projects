# import yfinance as yf
# import streamlit as st
# import pandas as pd


# tickers = ["ZAR=X", "EUR=X", "USD=X", "GBP=X"]

# data={}
# for ticker in tickers:
#     data[ticker] = yf.Ticker(ticker).history(period="40y")["Close"]


# st.write("""

# # Simple Stock Price App
#          South Africa vs European Close Price
#          """)


# combined_data = pd.DataFrame(data)
# st.line_chart(combined_data)


import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier


st.write("""
         # Iris Flower Prediction
         """)


st.sidebar.header("""
                 User Input Parameter
                 """)


def get_user_parameter():
    sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.84)
    sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.05)
    petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 3.76)
    petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 1.20)

    data = {
        "Sepal Length": sepal_length,
        "Sepal Width": sepal_width,
        "Petal Length": petal_length,
        "Petal Width": petal_width
    }

    features = pd.DataFrame(data, index=[0])

    return features


df = get_user_parameter()

st.write(df)

iris = load_iris()
X = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(X, y)


prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


st.subheader("""
            Cat labels and their corresponding index number
             """)
feature_names = pd.DataFrame(iris.target_names)
st.write(feature_names)


st.subheader("""
         Prediction
         """)
st.write(iris.target_names[prediction])

st.subheader("""
             Prediction Probability
             """)
st.write(prediction_proba)
