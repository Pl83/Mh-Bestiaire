from flask import Flask, render_template, jsonify
import requests
import jinja2 as jinja2


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/monsters')
def get_monsters():
    url = 'https://raw.githubusercontent.com/Pl83/Mh-Monster-data/main/data.json'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

