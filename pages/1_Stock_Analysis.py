import streamlit as st
from datetime import date as dt
from utils.CAPM_functions import *
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title= 'Stock Analysis', layout= 'wide')

st.title('Stock Analysis', width= 'stretch', text_alignment= 'center')

nifty500_list = get_list_nifty500()

company = nifty500_list['Company Name'].to_list()
symbol = nifty500_list['Symbol'].to_list()
yticker = nifty500_list['YahooTicker'].to_list()

niftydict = {}
for com, sym, ytick in zip(company, symbol, yticker):
    niftydict[com] = [sym, ytick]

user_stock = st.selectbox('Select Stock', company, company.index('Tata Consultancy Services Ltd.'))

longdescription, website, employees, fundamentals = get_info(niftydict[user_stock][1])

st.subheader(niftydict[user_stock][0])
st.write(longdescription)
col1, col2 = st.columns(2)
with col1:
    st.write(f"No. of Employees: {employees if employees is not None else 'Unknown'}")
with col2:
    st.write(f"Website: {website}")

st.subheader("Fundamentals")
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_table(fundamentals.iloc[0:6]))
with col2:
    st.plotly_chart(plot_table(fundamentals.iloc[6:12]))

user_stock_data = get_data_nifty500([niftydict[user_stock][1]], start= dt.today() - pd.DateOffset(20), end= dt.today(), include_market= False)
data = user_stock_data['Close']

daily_return_percent = (data.pct_change() * 100)[niftydict[user_stock][0]].iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric('Daily Change', round(data[niftydict[user_stock][0]].iloc[-1], 2), f"{round(daily_return_percent, 2)}%")

st.write('Historical Data (Last 10 days)')
last10 = user_stock_data.tail(10).sort_index(ascending= False).stack().round(2).reset_index()
last10.drop(columns= 'Ticker', inplace= True)
last10["Date"] = last10["Date"].dt.strftime("%Y-%m-%d")
st.plotly_chart(plot_table(last10, header_color="#182132", header_font_color= 'white'))

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns(12)

period = 365 # By default 1 year
with col1:
    if st.button('5D'):
        period = 5
with col2:
    if st.button('1M'):
        period = 30
with col3:
    if st.button('6M'):
        period = 30*6
with col4:
    if st.button('YTD'):
        period = (dt.today() - dt(dt.today().year,1,1)).days
with col5:
    if st.button('1Y'):
        period = 365
with col6:
    if st.button('5Y'):
        period = 365*5
with col7:
    if st.button('MAX'):
        period = 'max'

col1, col2, col3 = st.columns([1,1,4])
with col1:
    chart_type = st.selectbox('chart_type', ['Candle', 'Line'], label_visibility= 'hidden')
with col2:
    if chart_type == "Candle":
        indicator = st.selectbox('indic1', ['RSI', 'MACD'], label_visibility= 'hidden')
    else:
        indicator = st.selectbox('indic2', ['RSI', 'Moving Average', 'MACD'], label_visibility= 'hidden')

if period == 'max':
    new_data = get_data_nifty500([niftydict[user_stock][1]], include_market= False, max_period= True).stack().reset_index()
else:
    end = dt.today()
    start = end - pd.DateOffset(period)
    new_data = get_data_nifty500([niftydict[user_stock][1]], start= start, end= end, include_market= False).stack().reset_index()

if chart_type == "Candle" and indicator == "RSI":
    st.plotly_chart(candlestick(new_data))
    st.plotly_chart(RSI(new_data))

if chart_type == "Candle" and indicator == "MACD":
    st.plotly_chart(candlestick(new_data))
    st.plotly_chart(MACD(new_data))

if chart_type == "Line" and indicator == "RSI":
    st.plotly_chart(close_chart(new_data))
    st.plotly_chart(RSI(new_data))

if chart_type == "Line" and indicator == "Moving Average":
    st.plotly_chart(close_chart(new_data))
    st.plotly_chart(Moving_average(new_data))

if chart_type == "Line" and indicator == "MACD":
    st.plotly_chart(close_chart(new_data))
    st.plotly_chart(MACD(new_data))

