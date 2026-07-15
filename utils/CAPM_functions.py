import pandas as pd
import yfinance as yf
from plotly import express as px
import plotly.graph_objects as go
import numpy as np
from datetime import date as dt
import pandas_ta as pta
import warnings
warnings.filterwarnings('ignore')

def get_list_nifty500():
    url = "https://archives.nseindia.com/content/indices/ind_nifty500list.csv"
    nifty500_list = pd.read_csv(url)

    to_remove = ['DUMMYVEDL1', 'DUMMYVEDL3', 'DUMMYVEDL4', 'DUMMYVEDL2']
    nifty500_list = nifty500_list[~nifty500_list["Symbol"].isin(to_remove)]
    nifty500_list['YahooTicker'] = nifty500_list['Symbol'] + '.NS'

    return nifty500_list

def get_data_nifty500(tickers, start= None, end= None, include_market= True, max_period= False):
    if include_market :
        tickers = tickers + ["^CRSLDX"]
    if max_period:
        nifty500 = yf.download(tickers= tickers, # This will include market(Nifty500) data too
                period= 'max')
    else:
        nifty500 = yf.download(tickers= tickers, # This will include market(Nifty500) data too
                    start= start,
                    end= end)
    # Change the market name back to NIFTY500
    nifty500.rename(columns = {'^CRSLDX':'NIFTY500'}, inplace = True)

    # Change the tickers back to Symbols
    for col in nifty500.columns:
        if col != 'NIFTY500':
            nifty500 = nifty500.rename(columns={col[1]: col[1].split('.')[0]})
    return nifty500

def interactive_plot(df, include_market):
    fig = px.line()

    for col in df.columns:
        if col == 'NIFTY500' and include_market == False:
            continue #Don't include market if user doesn't want
        fig.add_scatter(x= df.index, y= df[col], name = col)
    fig.update_layout(width= 450, margin= dict(l=20, r=20, t=50, b=20), legend= dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1))
    return fig

def normalize_values(df):
    df_norm = df.copy()
    for col in df_norm.columns:
        df_norm[col] = df_norm[col]/df_norm[col].iloc[0]
    return df_norm

def daily_return(df):
    return df.pct_change()

def SCL(df, stock):
    # Security Characteristic Line
    temp = df[['NIFTY500', stock]].dropna()
    fig = px.scatter(
    temp,
    x="NIFTY500",
    y=stock,
    trendline="ols",
    trendline_color_override= 'red')

    return fig

def cal_beta(stock_daily_return, stock):
    temp = stock_daily_return[['NIFTY500', stock]].dropna()
    
    ''' Stock_return = b * Market_return + a'''
    b, a = np.polyfit(temp['NIFTY500'], temp[stock], 1)

    return b, a

def get_rm(period=10):
    # Calculate market return over 10 years every time (default)
    onlymarket = yf.download(tickers= ["^CRSLDX"],
                start= dt.today() - pd.DateOffset(365 * period),
                end= dt.today())
    return daily_return(onlymarket["Close"])['^CRSLDX'].mean() * 252 # About 252 trading days in a year

def get_info(ticker):
    yfticker = yf.Ticker(ticker)
    info = yfticker.info

    fundamentals = {
        "Market Cap": f"₹{info.get("marketCap") / 1e7:,.0f} Cr",
        "P/E (TTM)": info.get("trailingPE"),
        "P/B": info.get("priceToBook"),
        "ROE (%)": (
            round(info["returnOnEquity"] * 100, 2)
            if info.get("returnOnEquity") is not None else None
        ),
        "EPS (TTM)": info.get("trailingEps"),
        "Dividend Yield (%)": (
            round(info["dividendYield"] * 100, 2)
            if info.get("dividendYield") is not None else None
        ),
        "Debt-to-Equity": info.get("debtToEquity"),
        "52 Week High": info.get("fiftyTwoWeekHigh"),
        "52 Week Low": info.get("fiftyTwoWeekLow"),
        "Beta": info.get("beta"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry")
    }

    fundm = pd.DataFrame(
        columns= ['Metric', 'Values']
    )
    fundm['Metric'] = fundamentals.keys()
    fundm['Values'] = fundamentals.values()
    fundm["Values"] = fundm["Values"].astype(str)


    description = info.get('longBusinessSummary')
    ftEmployees = info.get('fullTimeEmployees')
    website = info.get('website')

    return description, website, ftEmployees, fundm

def plot_table(df: pd.DataFrame,
               odd_color: str = '#8faffd',
               even_color: str = "#F2F2F2",
               header_color: str = '#0e1117',
               header_font_color: str = None,
               height: int = None):

    if header_font_color == None:
        header_font_color = header_color

    if height is None:
        height = max(300, min(900, 40 * len(df) + 80))

    # Alternate row colors
    row_colors = [
        even_color if i % 2 == 0 else odd_color
        for i in range(len(df))
    ]

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=[f"<b>{col}</b>" for col in df.columns],
                    fill_color=header_color,
                    font=dict(color=header_font_color, size=13),
                    align="center",
                    height=35,
                ),
                cells=dict(
                    values=[df[col] for col in df.columns],
                    fill_color=[row_colors] * len(df.columns),
                    font=dict(color="#182132", size=15),
                    align="center",
                    height=30,
                ),
            )
        ]
    )

    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    return fig

def close_chart(dataframe):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Open"],
            mode="lines",
            name="Open",
            line=dict(width=2, color="#5ab7ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Close"],
            mode="lines",
            name="Close",
            line=dict(width=2, color="black"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["High"],
            mode="lines",
            name="High",
            line=dict(width=2, color="#0078ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Low"],
            mode="lines",
            name="Low",
            line=dict(width=2, color="red"),
        )
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        legend=dict(
            yanchor="top",
            xanchor="right",
            font=dict(color="black")
        ),
    )

    return fig

def candlestick(dataframe):

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=dataframe["Date"],
            open=dataframe["Open"],
            high=dataframe["High"],
            low=dataframe["Low"],
            close=dataframe["Close"],
        )
    )

    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
    )

    return fig

def RSI(dataframe):
    dataframe["RSI"] = pta.rsi(dataframe["Close"])

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["RSI"],
            name="RSI",
            marker_color="orange",
            line=dict(width=2, color="orange"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=[70] * len(dataframe),
            name="Overbought",
            marker_color="red",
            line=dict(width=2, color="red", dash="dash"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=[30] * len(dataframe),
            fill="tonexty",
            name="Oversold",
            marker_color="#79da84",
            line=dict(width=2, color="#79da84", dash="dash"),
        )
    )

    fig.update_layout(
        yaxis_range=[0, 100],
        height=200,
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="black")
        ),
    )

    return fig

def Moving_average(dataframe):

    dataframe["SMA_50"] = pta.sma(dataframe["Close"], 50)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Open"],
            mode="lines",
            name="Open",
            line=dict(width=2, color="#5ab7ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Close"],
            mode="lines",
            name="Close",
            line=dict(width=2, color="black"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["High"],
            mode="lines",
            name="High",
            line=dict(width=2, color="#0078ff"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Low"],
            mode="lines",
            name="Low",
            line=dict(width=2, color="red"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["SMA_50"],
            mode="lines",
            name="SMA 50",
            line=dict(width=2, color="purple"),
        )
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        legend=dict(
            yanchor="top",
            xanchor="right",
            font=dict(color="black")
        ),
    )

    return fig

def MACD(dataframe):
    macd = pta.macd(dataframe["Close"]).iloc[:, 0]
    macd_signal = pta.macd(dataframe["Close"]).iloc[:, 1]
    macd_hist = pta.macd(dataframe["Close"]).iloc[:, 2]

    dataframe["MACD"] = macd
    dataframe["MACD Signal"] = macd_signal
    dataframe["MACD Hist"] = macd_hist

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["MACD"],
            name="MACD",
            marker_color="orange",
            line=dict(width=2, color="orange"),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["MACD Signal"],
            name="MACD Signal",
            marker_color="red",
            line=dict(width=2, color="red", dash="dash"),
        )
    )

    c = ["red" if i < 0 else "green" for i in macd_hist]

    fig.add_trace(
        go.Bar(
            x=dataframe["Date"],
            y=dataframe["MACD Hist"],
            marker_color=c,
            name="MACD Histogram",
        )
    )

    fig.update_layout(
        height=200,
        plot_bgcolor="white",
        paper_bgcolor="#e1efff",
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="black")
        ),
    )

    return fig