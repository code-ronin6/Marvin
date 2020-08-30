import yfinance as yf
import json
import datetime as dt



date = dt.date.today()

wd = dt.date.weekday(date)

print(date)


keys, data = [], []


def get_quotes():
    if wd != 6 and wd != 5:
        stock_ticker = yf.Ticker("KO")
        stock_json = stock_ticker.history(start=str(date), end=str(date)).to_json(orient='split')
        clr_json = json.loads(stock_json)

        strs = clr_json['columns']
        data = clr_json['data'][0]

        return [strs, data]
    else:
        return None









get_quotes()

#TODO code doesn't responce quotes in normal table in Telegram
#TODO code doesn't responce normal quotes
#TODO code doesn't work with another stocks


