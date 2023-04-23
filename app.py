from flask import Flask, render_template, jsonify # pip install flask 
import requests # pip install requests
import jinja2 as jinja2 # pip install jinja2  (useless to call him here, but it's for the record)


app = Flask(__name__)
app.config['DEBUG'] = True


# template road (to associate the html files to the app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/monsters.html')
def monsters():
    return render_template('monsters.html')

@app.route('/details.html')
def details():
    return render_template('details.html')

@app.route('/weapons.html')
def weapons():
    return render_template('weapons.html')

@app.route('/type-list.html')
def type_list():
    return render_template('type-list.html')



# data road (to make data accessible on all pages)
@app.route('/api/monsters')
def get_monsters():
    url = 'https://raw.githubusercontent.com/Pl83/Mh-Monster-data/main/data_monsters.json'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/api/monsters/<string:name>')
def get_monster_by_name(name):
    url = 'https://raw.githubusercontent.com/Pl83/Mh-Monster-data/main/data_monsters.json'
    response = requests.get(url)
    datas = response.json()
    for data in datas['Monsters']:
        if data['name'] == name:
            return jsonify(data)
    return jsonify({'error': 'Monster not found'})
    

@app.route('/api/weapons')
def get_weapons():
    url = 'https://raw.githubusercontent.com/Pl83/Mh-Monster-data/main/data_weapons.json'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)