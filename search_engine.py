from lxml import html
import requests

CALDINING_URL='http://services.housing.berkeley.edu/FoodPro/dining/static/DiningMenus.asp?strCurLocation=0'
LIBRARY_URL="http://www.lib.berkeley.edu/hours#"
LIBRARIES=['anthropology library',
 'art history/classics library',
 'bancroft library/university archives',
 'berkeley law library',
 'bioscience & natural resources library',
 'business library',
 'career counseling library',
 'ced visual resources center',
 'chemistry library',
 'copy center',
 'data lab',
 'doe library',
 'earth sciences & map library',
 'east asian library',
 'education psychology library',
 'engineering library',
 'environmental design archives',
 'environmental design library',
 'ethnic studies library',
 'graduate services',
 'graduate theological union library',
 'institute for research on labor and employment library',
 'institute of governmental studies library',
 'institute of transportation studies library',
 'interlibrary services',
 'lawrence berkeley national laboratory library',
 'main stacks (gardner)',
 'mark twain papers & project',
 'mathematics statistics library',
 'media resources center',
 'moffitt library',
 'morrison library',
 'music library',
 'newspapers & microforms library',
 'northern regional library facility',
 'optometry and health sciences library',
 'pacific earthquake research (peer) center library',
 'pacific film archive library & film study center',
 'physics-astronomy library',
 'privileges desk',
 'public health library',
 'robbins collection',
 'social research library',
 'south/southeast asia library']

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

def get_library_hour(library):
    page = requests.get(LIBRARY_URL)
    html_tree = html.fromstring(page.content)
    hours = html_tree.xpath('//td[@class="library-hours-block"]/text()')
    new_hours = [x[3:len(x)-5] for x in hours if '-' in x or 'Closed' in x]
    if len(LIBRARIES) != len(new_hours):
        return "Not available"
    else:
        d = dict(zip(LIBRARIES, new_hours))
    hour = [d[l] for l in d if library in l][0]
    return hour
