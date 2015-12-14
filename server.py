from flask import Flask, render_template, request
import search_engine

m = {"crossroads": 1, "cafe3": 3, "ckc": 4, "foothill": 6}
libraries = ['anthropology library',
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

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def search_post():
    text = request.form['text'].lower()

    # search DH menus
    if text in m:
        #to-do: can only search non-duplicates
        menu = search_engine.get_menu_items(m[text])
        return render_template('home_menu.html', items = menu, name=text)

    # search library hours
    for l in libraries:
        if text in l:
            hour = search_engine.get_library_hour(text)
            return render_template('home_lib.html', text=hour)

    # search local current weather
    if text == "weather":
        weather = search_engine.get_weather()
        return render_template('home_weather.html', list = weather)

    return render_template('home_default.html')


if __name__ == '__main__':
    app.run(debug = True)
#to-do: pre-load the information before search to save time
#to-do: push to live
#to-do: use API Central to create personalized information search
