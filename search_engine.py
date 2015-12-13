from lxml import html
import requests

CALDINING_URL='http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?strCurLocation=0'

def get_menu_items(dining_hall_id):
    url = CALDINING_URL + str(dining_hall_id)
    page = requests.get(url)
    html_tree = html.fromstring(page.text)
    items = html_tree.xpath('//font/text()')
    return items[3:]

def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Berkeley&APPID=aa35616dabcb5d2225fabddac0a6d3ab"
    page = requests.get(url)
    info = page.json()
    temp = (info['main']['temp'] - 273.15) * 1.8 + 32
    return int(temp)
def change(x):
    return x + "gagaga"
