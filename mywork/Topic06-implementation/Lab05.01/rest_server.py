# rest_server.py

from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return jsonify({"message": "hello guest"})

@app.route("/books", methods=["GET"])
def getall():
    return jsonify({"message": "get all"})

@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    return jsonify({"message": f"find by id {id}"})

@app.route("/books", methods=["POST"])
def create():
    jsonstring = request.json
    return jsonify({"message": "create", "book": jsonstring})

@app.route("/books/<int:id>", methods=["PUT"])
def update(id):
    jsonstring = request.json
    return jsonify({"message": f"update book {id}", "book": jsonstring})

@app.route("/books/<int:id>", methods=["DELETE"])
def delete(id):
    return jsonify({"message": f"delete book {id}"})

if __name__ == "__main__":
    app.run(debug=True)