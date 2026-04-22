# 📈 DMart Stock Risk & Predictive Analysis

> A statistical and probabilistic approach to analyzing stock behaviour, risk, and future price trends with an interactive application.

---

## 📌 Overview

This project performs an in-depth analysis of DMart stock using statistical modeling, time-series techniques, and probabilistic methods.

It evaluates:

* Risk vs return characteristics
* Market behaviour using statistical tests
* Predictive patterns using stochastic models
* Interactive forecasting through a Streamlit application

---

## 🧠 Methodology

### 🔹 Data Processing

* Historical stock data (DMart & NIFTY)
* Return computation and cleaning

### 🔹 Exploratory Data Analysis (EDA)

* Price trends and return distributions
* Correlation with market index

### 🔹 Statistical Analysis

* Volatility estimation
* Sharpe ratio (risk-adjusted return)
* Normality and hypothesis testing

### 🔹 Trend Analysis

* Moving averages (20, 50, 200-day)
* Market behaviour insights

### 🔹 Advanced Modeling

* Markov Chains (state transitions)
* Hidden Markov Models (market regimes)
* Monte Carlo Simulation (future price scenarios)

---

## 🚀 Interactive Streamlit App

An interactive application is built to make the analysis usable in real-time.

### Features:

* 🔮 Next-day stock price prediction
* 📊 Sensitivity analysis under market shocks
* ⚠️ Risk metrics:

  * Volatility
  * Value at Risk (VaR)
  * Conditional VaR (CVaR)
  * Sharpe Ratio

### Run locally:

```bash
streamlit run app.py
```

---

## 📊 Key Insights

* DMart exhibits higher volatility compared to broader market indices
* Risk-adjusted returns indicate trade-offs between stability and growth
* Market regimes (bull/bear phases) can be identified using HMM
* Monte Carlo simulation provides probabilistic future price ranges

---

## ⚠️ Limitations

* Assumes historical patterns persist in future
* Simplified prediction model (mean return-based)
* External shocks and macroeconomic factors are not modeled

---

## 📁 Project Structure

```
Stock-Risk-Prediction-DMart/
│
├── dmart_analysis.ipynb
├── app.py
├── data/
│   ├── DMART_data.csv
│   └── NIFTY50_data.csv
├── README.md
└── requirements.txt
```
## 📄 Project Report

A detailed academic report is included covering:
- methodology
- statistical modeling
- theoretical background

File: `REPORT ON DMART.pdf`
---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* hmmlearn

---

## 👩‍💻 Author

Maryam Shaikh

MSc Applied Statistics

Interested in Data Science, Statistical Modeling, and Financial Analytics
