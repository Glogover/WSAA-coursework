# REST server example using Flask

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

#get all
@app.route("/books", methods=["GET"]) # Endpoint for getting all books
def getall():
    return "get all"

#get by id
@app.route("/books/<int:id>", methods=["GET"]) # Endpoint for getting a book by id, the <int:id> part means that the id will be passed as an integer parameter to the function
def findbyid(id):
    return f"find by id {id}"

#create
@app.route("/books", methods=["POST"]) # Endpoint for creating a new book
def create():
    # read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"

#update
@app.route("/books/<int:id>", methods=["PUT"]) # Endpoint for updating a book by id, the <int:id> part means that the id will be passed as an integer parameter to the function
def update(id):
    jsonstring = request.json  
    return f"update book {id} {jsonstring}"

#delete
@app.route("/books/<int:id>", methods=["DELETE"]) # Endpoint for deleting a book by id, the <int:id> part means that the id will be passed as an integer parameter to the function
def delete(id):
    return f"delete book {id}"

if __name__ == "__main__":
    app.run(debug=True)



