import yfinance as yf
import requests

def YahooStockPrice(ISIN, startDate, endDate):
        # Convert ISIN to symbol
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        params = {'q': ISIN, 'quotesCount': 1, 'newsCount': 0}
        r = requests.get(url, params=params)
        ticker_req = r.json()
        try:
                symbol = ticker_req['quotes'][0]['symbol']
        except IndexError:
                return print(str(ISIN) + ": Failed")
        data = yf.download(symbol, start=startDate, end=endDate)
        return data

