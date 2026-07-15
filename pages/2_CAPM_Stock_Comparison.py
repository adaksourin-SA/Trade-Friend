import streamlit as st
import pandas as pd
from datetime import date as dt
from utils.CAPM_functions import *
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title= 'CAPM Stock Comparison', layout= 'wide')

st.title('Capital Asset Pricing Model', width= 'stretch', text_alignment= 'center')

nifty500_list = get_list_nifty500()

company = nifty500_list['Company Name'].to_list()
symbol = nifty500_list['Symbol'].to_list()
yticker = nifty500_list['YahooTicker'].to_list()

niftydict = {}
for com, sym, ytick in zip(company, symbol, yticker):
    niftydict[com] = [sym, ytick]

col1, col2 = st.columns([1,1])

with col1:
    user_stock_list = st.multiselect('Choose Stocks', company, ['Reliance Industries Ltd.', 'ITC Ltd.', 'Tata Consultancy Services Ltd.', 'Maruti Suzuki India Ltd.'])
with col2:
    period = st.number_input('Number of Years', 1, 10)

end = dt.today()
start = end - pd.DateOffset(365 * period)
stock_data = get_data_nifty500([niftydict[com][1] for com in user_stock_list], start= start, end= end)['Close']

with col1:
    st.markdown('### Oldest')
    st.dataframe(stock_data.head(), width= 'stretch')

with col2:
    st.markdown('### Latest')
    st.dataframe(stock_data.tail(), width= 'stretch')

with col1:
    st.markdown('### Price Chart')
    col11, col12 = st.columns(2)
    with col11:
        incm = st.checkbox(label= 'Include Market', value= True, key= 'include_market')
    with col12:
        isnorm = st.checkbox(label= 'Normalize', value= False, key= 'Normalize')

    if isnorm:
        st.plotly_chart(interactive_plot(normalize_values(stock_data), incm))
    else:
        st.plotly_chart(interactive_plot(stock_data, incm))

df_daily_return = daily_return(stock_data) # Calculate daily return for each stock+market

beta = {}
alpha = {}
for col in df_daily_return.columns:
    if col != 'NIFTY500':
        b, a = cal_beta(df_daily_return, col)
        beta[col] = b
        alpha[col] = a

# Stocks along with their beta values
betaframe = pd.DataFrame({'Stock': list(beta.keys()),
                          'Beta Values' : list(beta.values())})

# Risk Free return : The Indian 10-year government bond yield stands at approximately 6.72%
rf = 0.0672
rm = get_rm()

return_val = []

for stock, value in beta.items():
    return_val.append(round(rf + value * (rm - rf), 4))

# Stocks along with their expected returns
return_df = pd.DataFrame({'Stock' : list(beta.keys()),
                          '% Return' : [i * 100 for i in return_val]})

with col2:
    st.markdown("""
    ### Beta Estimation <span style="font-size:0.6em; font-weight:normal;"><sup>*Over chosen period</sup></span>
    """, unsafe_allow_html=True)
    col11, col12 = st.columns(2)
    with col11:
        user_stock = st.selectbox('Select Stock', [niftydict[com][0] for com in user_stock_list])
    with col12:
        st.markdown(f"**Exp. Annual Return: {round(return_df.loc[return_df['Stock'] == user_stock, '% Return'].iloc[0], 2)}%**", width= 'stretch', text_alignment= 'right')
    st.plotly_chart(SCL(df_daily_return, user_stock))

col1, col2 = st.columns(2) # New columns were made to align the dataframes
with col1:
    st.markdown("""
    ### Beta Comparison <span style="font-size:0.6em; font-weight:normal;"><sup>*Over chosen period</sup></span>
    """, unsafe_allow_html=True)
    st.dataframe(betaframe, width= 'stretch')

with col2:
    st.markdown("""
    ### CAPM Return Estimates <span style="font-size:0.6em; font-weight:normal;"><sup>*Computed market return over 10Y</sup></span>
    """, unsafe_allow_html=True)
    st.dataframe(return_df, width= 'stretch')