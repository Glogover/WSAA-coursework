from mywork.hello import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
# To run the Flask application, use the command:
# python mywork/flask.py    