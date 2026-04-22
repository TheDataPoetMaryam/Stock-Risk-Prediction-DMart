import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load historical data and force numeric conversion
data = pd.read_csv("DMART_data.csv")

# Make sure 'Close' is numeric (in case it's being read as string)
data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

# Drop any rows where 'Close' was invalid
data = data.dropna(subset=['Close'])

# Now returns will work
returns = data['Close'].pct_change(fill_method=None).dropna()


st.title("📈 DMart Stock Price Predictor & Risk Analyzer")

# Input today's price
today_price = st.number_input("Enter today's stock price (₹):", min_value=100.0, step=1.0)

if st.button("Predict"):
    # Tomorrow's prediction (replace with your model if needed)
    predicted_price = today_price * (1 + returns.mean())
    st.success(f"Predicted tomorrow's price: ₹{predicted_price:.2f}")

    # Sensitivity analysis
    shocks = [-0.2, -0.1, -0.05, 0.05, 0.1, 0.2]
    sensitivity_results = {}
    for shock in shocks:
        new_price = today_price * (1 + shock)
        predicted = new_price * (1 + returns.mean())
        sensitivity_results[f"{shock*100:.0f}% change"] = round(float(predicted), 2)

    df = pd.DataFrame(list(sensitivity_results.items()), columns=["Shock", "Predicted Price"])
    st.write("### 🔎 Sensitivity Analysis")
    st.dataframe(df)

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(df["Shock"], df["Predicted Price"])
    ax.set_title("Sensitivity Analysis of DMart Predicted Price")
    ax.set_xlabel("Shock in Today's Price")
    ax.set_ylabel("Predicted Tomorrow's Price (₹)")
    st.pyplot(fig)

    # Risk Analysis
    st.write("### ⚠️ Risk Analysis")

    volatility = np.std(returns) * np.sqrt(252)  # annualized
    VaR_95 = np.percentile(returns, 5)
    CVaR_95 = returns[returns <= VaR_95].mean()
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252)

    risk_metrics = {
        "Annualized Volatility": round(volatility, 4),
        "VaR (95%)": round(VaR_95, 4),
        "CVaR (95%)": round(CVaR_95, 4),
        "Sharpe Ratio": round(sharpe_ratio, 2)
    }

    st.write(risk_metrics)


