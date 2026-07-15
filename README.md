# 📈 Trade Friend

> **A comprehensive Stock Analysis Dashboard for the Indian Stock Market built with Streamlit, Plotly, Yahoo Finance and Python.**

Trade Friend is an interactive web application designed to help investors and finance enthusiasts analyze Indian stocks using modern visualization techniques and financial models. The application currently provides company fundamentals, technical analysis, and Capital Asset Pricing Model (CAPM) based stock comparison.

> 🚧 **This repository is under active development.**
>
> This is **Part 1** of the project. The next phase will introduce **Machine Learning based Stock Price Prediction**.

---

## 🚀 Live Demo

🌐 **Web App:** [Streamlit Web App](https://trade-friend.streamlit.app/)

---

# 📖 Overview

Trade Friend aims to provide an easy-to-use dashboard for analyzing stocks listed in the **NIFTY 500 Index**.

Instead of switching between multiple financial websites, users can access company information, historical market data, technical indicators, and CAPM analysis from a single interactive application.

The project is divided into multiple modules that will be released incrementally.

## Current Release (Part 1)

- 📊 Company Overview
- 📈 Interactive Price Charts
- 📉 Technical Indicators
- 📋 Historical Market Data
- 📐 CAPM Stock Comparison
- 📊 Beta Estimation
- 📈 Expected Return using CAPM

## Upcoming Release (Part 2)

- 🤖 Machine Learning based Stock Price Prediction
- 📈 Future Price Forecasting
- 📊 Model Performance Evaluation

---

# ✨ Features

## 📊 Stock Overview

Explore detailed information for any stock listed in the NIFTY 500.

Current information includes:

- Company Description
- Website
- Number of Employees
- Market Capitalization
- P/E Ratio
- P/B Ratio
- ROE
- EPS
- Dividend Yield
- Debt-to-Equity
- Beta
- 52 Week High & Low
- Sector
- Industry

---

## 📈 Interactive Price Charts

Visualize stock prices using interactive Plotly charts.

Supported chart types:

- Line Chart
- Candlestick Chart

Users can explore historical price movements across multiple timeframes.

Supported durations:

- 5 Days
- 1 Month
- 6 Months
- Year-to-Date
- 1 Year
- 5 Years
- Maximum Available History

---

## 📉 Technical Indicators

The application currently supports:

- Relative Strength Index (RSI)
- Moving Average (SMA 50)
- MACD

These indicators help identify trends, momentum, and potential buy/sell signals.

---

## 📋 Historical Data

View recent historical market data including:

- Open
- High
- Low
- Close
- Volume

along with daily percentage change.

---

## 📐 CAPM Stock Comparison

Compare multiple NIFTY 500 stocks using the Capital Asset Pricing Model.

Features include:

- Multi-stock comparison
- Historical price comparison
- Price normalization
- Beta estimation
- Expected annual return estimation
- Security Characteristic Line (SCL)

---

## 📊 Interactive Visualization

Built using Plotly for a fully interactive experience.

Features include:

- Zoom
- Pan
- Hover Information
- Dynamic Legends
- Interactive Tables

---

# 🧮 Financial Models Used

## Capital Asset Pricing Model (CAPM)

Expected return is estimated using

$$
E(R_i)=R_f+\beta_i(R_m-R_f)
$$ 


where

- **Rf** = Risk-Free Rate
- **Rm** = Expected Market Return
- **β** = Beta

---

## Beta Estimation

Beta is estimated using linear regression between

- Market Returns
- Stock Returns

to measure the systematic risk of each stock.

---

## Security Characteristic Line (SCL)

Visualizes the relationship between

- Market Return
- Stock Return

along with the regression line used to estimate beta.

---

# 🎬 Application Demo

## Home Page

> **GIF Placeholder**

```text
assets/gifs/home_page.gif
```

---

## Company Overview

> **GIF Placeholder**

```text
assets/gifs/company_overview.gif
```

---

## Technical Indicators

> **GIF Placeholder**

```text
assets/gifs/technical_indicators.gif
```

---

## CAPM Dashboard

> **GIF Placeholder**

```text
assets/gifs/capm_dashboard.gif
```

---

## Stock Comparison

> **GIF Placeholder**

```text
assets/gifs/stock_comparison.gif
```

---

## Security Characteristic Line

> **GIF Placeholder**

```text
assets/gifs/security_characteristic_line.gif
```
---

# 📂 Project Structure

```text
Trade_Friend/
│
├── pages/
│   └── CAPM_Stock_Comparison.py      # CAPM Stock Comparison dashboard
│
├── utils/
│   ├── __init__.py
│   └── CAPM_functions.py             # Utility functions
│
├── Get_Data.ipynb                    # Experimental notebook (development only)
├── Trade_Friend.py                   # Main Streamlit application
├── requirements.txt
└── README.md
```

> **Note:** `Get_Data.ipynb` is an exploratory notebook used during development to experiment with Yahoo Finance APIs, calculations, and helper functions. It is not part of the production application.

---

# ⚙️ Tech Stack

### Programming Language

- Python

### Web Framework

- Streamlit

### Data Processing

- Pandas
- NumPy

### Financial Data

- Yahoo Finance (`yfinance`)

### Visualization

- Plotly

### Technical Analysis

- pandas-ta

### Statistical Analysis

- NumPy
- Statsmodels

---

# 📊 Data Sources

Financial market data is obtained from:

- Yahoo Finance

Market Benchmark:

- NIFTY 500 Index

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/<username>/Trade_Friend.git
```

Navigate to the project directory

```bash
cd Trade_Friend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the Streamlit app

```bash
streamlit run Trade_Friend.py
```

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are always welcome.

If you would like to contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Sourin Adak**

**Data Analytics | Financial Analytics | Python Developer**

---

# ⭐ Support the Project

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps the project reach more people and motivates future development.

---

## 📢 Upcoming

🚀 **Trade Friend – Part 2**

The next update will introduce **Machine Learning based Stock Price Prediction**, allowing users to forecast future stock prices using predictive models alongside the existing analytical dashboard.