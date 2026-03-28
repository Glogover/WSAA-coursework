# REST server example using Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/books", methods=["GET"])
def getall():
    return "get all"

@app.route("/books/<int:id>", methods=["GET"])
def findbyid(id):
    return f"find by id {id}"


if __name__ == "__main__":
    app.run(debug=True)



