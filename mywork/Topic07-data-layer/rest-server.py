# flask server that links to a DAO

from flask import Flask, request, jsonify, abort
from bookDAO-skeleton import bookDAO


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
    return jsonify(bookDAO.get_all())


# find by id
# curl http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['GET'])
def find_by_id(id):
    return jsonify(bookDAO.find_by_id(id))

# create
# curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\": 123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    # read json from the body
    jsonstring  = request.json
    book = {}

    if "title" not in jsonstring:
            abort(401)
    book["title"] = jsonstring["title"]
    if "author" not in jsonstring:
            abort
    book["author"] = jsonstring["author"]
    if "price" not in jsonstring:
            abort(401)
    book["price"] = jsonstring["price"]

    return jsonify(bookDAO.create(book))

# update








