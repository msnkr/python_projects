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
iris = load_iris()

st.sidebar.write("""
                 Iris Dataset
                 """)
                 

df = pd.DataFrame()