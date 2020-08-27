import requests
import json
import datetime as dt


def get_ph_nasa():
    date = str(dt.date.today())



    url = "https://api.nasa.gov/planetary/apod?api_key=nTM2vgjf82xOL2OcecNWQEwxkyFnEjmauGn7qHkP"
    params = {"date" : date}

    data = requests.get(url, params).text # получаем содержание страницы

    json_data = json.loads(data)
    return [json_data["url"], json_data['title'], json_data["explanation"]]


get_ph_nasa()




