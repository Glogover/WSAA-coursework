# flask server that links to a DAO

from flask import Flask, request, jsonify, abort
from bookDAO import bookDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
        return "Hello world"

# getall
@app.route('/books', methods=['GET'])
def getall():
        return jsonify(bookDAO.getAll())

# find by id
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(bookDAO.findByID(id))

# create
@app.route('/books', methods=['POST'])
def create():
        jsonstring = request.json
        book = {}

        if "title" not in jsonstring:
                abort(403)
        book["title"] = jsonstring["title"]

        if "author" not in jsonstring:
                abort(403)
        book["author"] = jsonstring["author"]

        if "price" not in jsonstring:
                abort(403)
        book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.create(book))

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    book = {}

    if "title" in jsonstring:
        book["title"] = jsonstring["title"]
    if "author" in jsonstring:
        book["author"] = jsonstring["author"]
    if "price" in jsonstring:
        book["price"] = jsonstring["price"]

    bookDAO.update(id, book)

    # FIX: return something so Flask can jsonify it
    return jsonify({"status": "updated"}), 200



# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        bookDAO.delete(id)
        return jsonify({"status": "deleted"}), 200   # ← FIX


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


