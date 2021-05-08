import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")
print("History:")
print(hist)
print("-------------------------------------------------")

# show actions (dividends, splits)
print(msft.actions)

# show dividends
msft.dividends

# show splits
msft.splits

# show financials
print("-------------------------------------------------")
print("Financials")
print(msft.financials)
print(msft.quarterly_financials)
print("-------------------------------------------------")

# show major holders
msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
msft.balance_sheet
msft.quarterly_balance_sheet

# show cashflow
msft.cashflow
msft.quarterly_cashflow

# show earnings
msft.earnings
msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations
msft.recommendations

# show next event (earnings, etc)
msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations
msft.options
