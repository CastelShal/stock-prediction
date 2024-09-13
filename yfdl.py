import yfinance as yf
data = yf.download("AAPL", start='2021-05-17', end='2024-09-05')
data.to_csv("data/stock.csv")
