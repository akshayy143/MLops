import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.write(
    """
    # Stock Price App 
    """
)

tickerSymbol = st.text_input("Enter stock ticker symbol", "AAPL",
                              key="placeholder")
## AAPL stock symbol of Apply company
# tickerSymbol = "AAPL"


start_date = st.date_input(
    "Start date",
    datetime.datetime(2019,1,1) ##knhh
)

end_date = st.date_input(
    "End date",
    datetime.datetime(2022,12,31)
)

## Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
## Get the historical prices for this ticker
tickerDf = tickerData.history(
                              start="2019-01-01",
                              end = "2022-12-31")

st.dataframe(tickerDf)   

st.write(
    """
    ## Closing Price
    """
)
st.line_chart(tickerDf.Close)


st.write(
    """
    ## Volume
    """
)
st.line_chart(tickerDf.Volume)

