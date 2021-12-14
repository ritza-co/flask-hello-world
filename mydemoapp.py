from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print('Github testing....')
    return "Hello! This is a basic Flask app. "

if __name__ == "__main__":
    app.run("0.0.0.0")


