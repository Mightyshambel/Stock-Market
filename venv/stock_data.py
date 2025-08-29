import yfinance as yf

# Create a Ticker object for Microsoft (MSFT)
msft = yf.Ticker("MSFT")

# Download historical data (maximum available)
msft_data = msft.history(period="max")

# Display the first 5 rows
print(msft_data.head())
