import flask
import operations as op
from flask import request
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route("/notes", methods=['GET'])
def getNotes():
    return op.getNotes()

@app.route("/notes", methods=['POST'])
def addNote():
    note = request.data
    return op.addNote(note)

@app.route("/notes/delete/<id>", methods=['DELETE'])
def deleteNote(id):
    return op.deleteNote(id)

app.run(host="0.0.0.0", port=5000)