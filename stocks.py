import yfinance as yf
import json
import datetime as dt
import tabulate


date = dt.date.today()



def get_quotes():
    stock = yf.Ticker("TSLA")
    js_string = stock.history(start=str(date), end=str(date)).to_json()
    js = json.loads(js_string)

    columns, rows = [], [()]

    for x in js.keys():
        columns.append(x)
        rows = [((str(list(js.values())[i]['1597708800000'])) for i in range(0, 7))]

    print(tabulate.tabulate(tabular_data=rows, headers=columns))
    return tabulate.tabulate(tabular_data=rows, headers=columns)


get_quotes()

#TODO code doesn't responce quotes in normal table in Telegram
#TODO code doesn't responce normal quotes
#TODO code doesn't work with another stocks


