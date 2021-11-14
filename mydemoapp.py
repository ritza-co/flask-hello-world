from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! This is a basic Flask app. "

@app.route("/<name>")
def hello_name(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run("0.0.0.0")
