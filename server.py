from flask import Flask, render_template, request
import search_engine
m = {"crossroads": 1, "cafe3": 3, "ckc": 4, "foothill": 6}
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def search_post():
    text = request.form['text']
    string = search_engine.change(text)
    # search DH menus
    if text in m:
        menu = search_engine.get_menu_items(m[text])
        return render_template('home_menu.html', items = menu)
    # search local current weather
    if text == "weather":
        weather = search_engine.get_weather()
        return render_template('home_weather.html', string = weather)
    return render_template('home_test.html')

if __name__ == '__main__':
    app.run(debug = True)






# hold on
