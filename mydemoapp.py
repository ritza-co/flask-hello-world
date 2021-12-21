from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! This is a basic Flask app. I am adding this quote to demonstrate my contribution to this project. "

if __name__ == "__main__":
    app.run("0.0.0.0")
