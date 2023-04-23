from flask import Flask, render_template, jsonify
import requests
import jinja2 as jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

# template road
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details.html')
def details():
    return render_template('details.html')

@app.route('/weapons.html')
def weapons():
    return render_template('weapons.html')



# data road
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