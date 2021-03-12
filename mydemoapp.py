from flask import Flask

app = Flask(__name__)

line="==================== WELCOME to BasicFLASK! ==================="
@app.route("/")
def init():
    return line

@app.route("/<name>")
def personalised(name):
    return f"Hello {name}"
    
if __name__ == "__main__":
    app.run("0.0.0.0")
