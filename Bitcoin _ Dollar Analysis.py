
import pandas as pd
import matplotlib.pyplot as plt

# Load the simulated BTC data
df = pd.read_csv("simulated_btc.csv", parse_dates=["Date"], index_col="Date")

# Add WeekDay column
df["WeekDay"] = df.index.weekday

# Initialize sarmaeh and BTC balance
sarmaeh = 1000.0
mojodi_BTC = 0.0
portfolio_values = []
dates = []

# Simulate buying on Wednesdays (weekday 2) and selling on Fridays (weekday 4)
for i in range(len(df) - 1):
    row = df.iloc[i]
    next_row = df.iloc[i + 1]

    if row["WeekDay"] == 2:  # Wednesday: Buy at Open
        if sarmaeh > 0:
            mojodi_BTC = sarmaeh / row["Open"]
            sarmaeh = 0.0

    elif row["WeekDay"] == 4:  # Friday: Sell at Close
        if mojodi_BTC > 0:
            sarmaeh = mojodi_BTC * row["Close"]
            mojodi_BTC = 0.0

    # Calculate current portfolio value
    current_price = row["Close"]
    portfolio_value = sarmaeh + (mojodi_BTC * current_price)
    portfolio_values.append(portfolio_value)
    dates.append(row.name)

# Final portfolio value
Dadeh_nahaei = sarmaeh + (mojodi_BTC * df.iloc[-1]["Close"])

# Plot the portfolio value over time
plt.figure(figsize=(12, 6))
plt.plot(dates, portfolio_values, label="Portfolio Value", color="Blue")
plt.title("Portfolio Value Over Time (Buy on Wed, Sell on Fri)")
plt.xlabel("Date")
plt.ylabel("Value (USD)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

