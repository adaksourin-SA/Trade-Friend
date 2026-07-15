import streamlit as st

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="Trade Friend",
    page_icon="📈",
    layout="wide",
)

# -------------------------------------------------------
# CSS
# -------------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#0F172A;
}

.hero{
    background:linear-gradient(135deg,#0f172a,#1e3a8a);
    padding:45px;
    border-radius:18px;
    color:white;
}

.hero h1{
    color:white;
    font-size:48px;
    margin-bottom:10px;
}

.hero p{
    color:#dbeafe;
    font-size:20px;
}

.card{
    background:#F8FAFC;
    border:1px solid #E2E8F0;
    border-radius:16px;
    padding:22px;
}

.metric{
    text-align:center;
    padding:15px;
    border-radius:12px;
    background:#F8FAFC;
    border:1px solid #E2E8F0;
}

.small{
    color:gray;
    font-size:14px;
}

.module{
    background:#F8FAFC;
    border-radius:18px;
    border:1px solid #CBD5E1;
    padding:30px;
}

.module h3{
    margin-bottom:10px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# HERO
# -------------------------------------------------------

left, right = st.columns([2.4,1])

with left:

    st.markdown("""
    <div class='hero'>

    # 📈 Trade Friend

    **Analyze • Compare • Understand • Invest**

    Trade Friend is an interactive stock analytics platform
    built for the Indian stock market.

    Explore company fundamentals, visualize historical prices,
    analyze technical indicators and compare stocks using
    the Capital Asset Pricing Model (CAPM).

    </div>
    """, unsafe_allow_html=True)

with right:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2784/2784445.png"
    )

st.write("")

# -------------------------------------------------------
# WHY TRADE FRIEND
# -------------------------------------------------------

st.header("✨ Why Trade Friend?")

col1,col2,col3,col4 = st.columns(4)

with col1:
    with st.container(border=True):

        st.markdown("## 📊")

        st.subheader("Company Analysis")

        st.write("""
- Company Overview
- Business Summary
- Market Capitalization
- Financial Ratios
- Sector & Industry
""")

with col2:
    with st.container(border=True):

        st.markdown("## 📈")

        st.subheader("Technical Charts")

        st.write("""
- Candlestick Charts
- RSI
- Moving Average
- MACD
- Historical Prices
""")

with col3:
    with st.container(border=True):

        st.markdown("## 📉")

        st.subheader("CAPM")

        st.write("""
- Beta Estimation
- Expected Return
- Market Comparison
- Price Normalization
- Risk Analysis
""")

with col4:
    with st.container(border=True):

        st.markdown("## ⚡")

        st.subheader("Interactive")

        st.write("""
- Plotly Charts
- Fast Data Loading
- Interactive Tables
- Live Market Data
- Clean Dashboard
""")

st.divider()

# -------------------------------------------------------
# MODULES
# -------------------------------------------------------

st.header("🚀 Explore Modules")

left,right = st.columns(2)

# ---------------- STOCK ANALYSIS ----------------

with left:

    with st.container(border=True):

        st.markdown("## 📊 Stock Analysis")

        st.caption(
            "Analyze any company listed in the NIFTY 500."
        )

        st.write("")

        f1,f2 = st.columns(2)

        with f1:
            st.write("✅ Company Profile")
            st.write("✅ Fundamentals")
            st.write("✅ Historical Data")
            st.write("✅ Price Charts")

        with f2:
            st.write("✅ RSI")
            st.write("✅ MACD")
            st.write("✅ Moving Average")
            st.write("✅ Daily Change")

        st.write("")

        st.page_link(
            "pages/1_Stock_Analysis.py",
            label="Open Stock Analysis",
            icon="📊"
        )

# ---------------- CAPM ----------------

with right:

    with st.container(border=True):

        st.markdown("## 📈 CAPM Comparison")

        st.caption(
            "Compare multiple stocks using CAPM."
        )

        st.write("")

        f1,f2 = st.columns(2)

        with f1:
            st.write("✅ Beta")
            st.write("✅ Expected Return")
            st.write("✅ Price Comparison")
            st.write("✅ Market Benchmark")

        with f2:
            st.write("✅ Security Line")
            st.write("✅ Multi-stock Analysis")
            st.write("✅ Normalization")
            st.write("✅ Interactive Graphs")

        st.write("")

        st.page_link(
            "pages/2_CAPM_Stock_Comparison.py",
            label="Open CAPM Comparison",
            icon="📈"
        )

st.divider()

# -------------------------------------------------------
# WORKFLOW
# -------------------------------------------------------

st.header("📌 How Trade Friend Works")

st.write("")

step1, step2, step3, step4 = st.columns(4)

with step1:
    with st.container(border=True):
        st.markdown("## ①")
        st.subheader("Choose a Stock")
        st.write(
            "Select any company listed in the NIFTY 500 universe."
        )

with step2:
    with st.container(border=True):
        st.markdown("## ②")
        st.subheader("Analyze")
        st.write(
            "Explore company profile, financial ratios and historical market data."
        )

with step3:
    with st.container(border=True):
        st.markdown("## ③")
        st.subheader("Visualize")
        st.write(
            "Study price action using interactive charts and technical indicators."
        )

with step4:
    with st.container(border=True):
        st.markdown("## ④")
        st.subheader("Compare")
        st.write(
            "Estimate Beta and Expected Return using the Capital Asset Pricing Model."
        )

st.divider()

# -------------------------------------------------------
# TECH STACK
# -------------------------------------------------------

st.header("🛠 Technology Stack")

row1 = st.columns(4)

with row1[0]:
    st.metric("🐍 Python", "3.13.13")

with row1[1]:
    st.metric("⚡ Streamlit", "Frontend")

with row1[2]:
    st.metric("📊 Plotly", "Interactive Charts")

with row1[3]:
    st.metric("💹 yFinance", "Market Data")

row2 = st.columns(4)

with row2[0]:
    st.metric("🐼 Pandas", "Data Processing")

with row2[1]:
    st.metric("🔢 NumPy", "Numerical Computing")

with row2[2]:
    st.metric("📉 pandas-ta", "Technical Indicators")

with row2[3]:
    st.metric("📈 Statsmodels", "Regression")

st.divider()

# -------------------------------------------------------
# FEATURES SUMMARY
# -------------------------------------------------------

st.header("📋 Current Features")

left, right = st.columns(2)

with left:

    st.success("### 📊 Stock Analysis")

    st.write("""
✅ Company Overview

✅ Business Summary

✅ Market Capitalization

✅ Financial Ratios

✅ Historical Market Data

✅ Daily Price Change

✅ Candlestick Charts

✅ RSI

✅ MACD

✅ Moving Average

✅ Interactive Plotly Charts
""")

with right:

    st.success("### 📈 CAPM Comparison")

    st.write("""
✅ Multiple Stock Comparison

✅ Market Benchmark

✅ Price Normalization

✅ Beta Estimation

✅ Expected Annual Return

✅ Security Characteristic Line

✅ Interactive Scatter Plots

✅ Historical Price Comparison
""")

st.divider()

# -------------------------------------------------------
# ABOUT
# -------------------------------------------------------

st.header("👨‍💻 About Trade Friend")

st.write("""
Trade Friend is a financial analytics application built for the Indian stock market.

The objective of this project is to provide investors, students, and finance
enthusiasts with an intuitive platform for exploring company fundamentals,
technical analysis, and quantitative financial models.

The application currently supports:

- 📊 Fundamental Analysis
- 📈 Technical Analysis
- 📉 CAPM-based Stock Comparison

Future releases will integrate Machine Learning models to provide stock price
forecasting and portfolio analytics.
""")

st.divider()

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------

st.markdown(
    """
    <div style='text-align:center; padding:20px 0; color:gray;'>

    <h3>📈 Trade Friend</h3>

    <p>
    Built with ❤️ using <b>Python</b>, <b>Streamlit</b>,
    <b>Plotly</b> and <b>Yahoo Finance</b>.
    </p>

    <p>
    © 2026 Sourin Adak
    </p>

    </div>
    """,
    unsafe_allow_html=True,
)