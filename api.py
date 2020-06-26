import flask
from flask_cors import CORS, cross_origin
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    JSONToReturn = '{ "Ander":"Guapo"}'
    return json.loads(JSONToReturn)

@app.route("/ander", methods=["GET"])
@cross_origin()
def ander():
    return "hola"
app.run()
