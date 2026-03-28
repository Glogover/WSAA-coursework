from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "hello mum"

@app.route("/inquery")
def inquery():
    name = request.args.get("name")
    return name
    #return request.args



if __name__ == "__main__":
    app.run(debug=True)

