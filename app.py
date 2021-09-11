import flask
from flask import request, request, jsonify
import json
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open(r'C:\Users\Lucas\OneDrive\Desktop\flask stuff\coelacanth API\a.json') as f:
    facts = json.load(f)

@app.route('/', methods=['GET'])
def home():
    data = open("static/index.html").read()
    return data

@app.route('/api/v1/resources/facts/all', methods=['GET'])
def api_all():
    return jsonify(facts)

@app.route('/api/v1/resources/facts/random', methods=['GET'])
def myRandom():
    return jsonify(random.choice(facts))

@app.route('/api/v1/resources/facts', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    
    results = []

    for fact in facts:
        if fact['id'] == id:
            results.append(fact)

    return jsonify(results)

if __name__ == "__main__":
    app.run()