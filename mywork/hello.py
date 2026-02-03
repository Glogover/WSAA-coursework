from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run()
# To run the Flask application, use the command:
# python mywork/flask.py  
# Then open your web browser and go to http://127.0.0.1:5000
# You should see "Hello, Flask!" displayed in your browser.  