import yfinance as yf
import json
import datetime as dt



date = dt.date.today()
print(date)

keys, data = [], []


def get_quotes():
    stock_ticker = yf.Ticker("KO")
    stock_json = stock_ticker.history(start=str(date), end=str(date)).to_json(orient='split')
    clr_json = json.loads(stock_json)
    print(type(clr_json))
    print(clr_json)

    strs = clr_json['columns']
    data = clr_json['data'][0]

    return [strs, data]






get_quotes()

#TODO code doesn't responce quotes in normal table in Telegram
#TODO code doesn't responce normal quotes
#TODO code doesn't work with another stocks


