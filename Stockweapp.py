import requests
import streamlit as st
import pandas as pd

apikey = "D4FTLHPX7MUGHTXA"
st.sidebar.header("**stock Symbol**")
symbol = st.sidebar.selectbox(
    'which stocks you have',
   ('DOX','c', 'TCS', 'AMZN',  'MSFT', 'TM', 'VOD', 'INTC', 'PEP', 'DELL', 'MS', 'ORCL', 'GS', 'AAPL', 'EBAY', 'MOT', 'CAJ', 'HMC', 'YHOO',
    'WIT', 'INFY', 'ACN', 'SNDK', 'PBG'))

#url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey={apikey}'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&apikey={apikey}'
r = requests.get(url)
data = r.json()
st.title(f'{symbol} portfolio')
data = pd.DataFrame(data['Time Series (15min)'])
data = data.T
st.write(data.head(10))

st.line_chart(data['1. open'].head(10))
st.line_chart(data['4. close'].head(10))
