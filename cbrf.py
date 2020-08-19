import datetime
import requests
import json

def get_rates(valute):
    get_curl = "https://www.cbr-xml-daily.ru/daily_json.js"
    # формат день/месяц/год
    date_format = "%Y/%m/%d"
    # дата запроса
    today = datetime.datetime.today()
    params = {"date_req" : today.strftime(date_format)}
    r = requests.get(get_curl, params=params)
    resp = r.text
    data = json.loads(resp)
    name = data['Valute'][valute]['Name']
    value = data['Valute'][valute]['Value']
    nominal = data['Valute'][valute]['Nominal']
    responce_from_bot = str(nominal) + " " + name + ' : ' + str(value) + " руб."
    responce_from_bot = ''.join(map(str, (responce_from_bot)))
    return responce_from_bot
##########################
# needs only for developing
def get_info():
    hash = {}
    get_curl = "https://www.cbr-xml-daily.ru/daily_json.js"
    date_format = "%Y/%m/%d"
    today = datetime.datetime.today()
    params = {"date_req" : today.strftime(date_format)}
    r = requests.get(get_curl, params=params)
    resp = r.text
    data = json.loads(resp)
    for i in data['Valute']:
        hash[data['Valute'][i]['Name']] = str(i)
    #string = ''.join(map(str, string))
    return str(hash)

get_info()

