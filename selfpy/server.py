from flask import Flask
app = Flask(__name__)


@app.route("/a")
def hello():
    return "<h2>a?"

@app.route("/hello")
def mo():
    return "<h2>Hello again!"

@app.route("/bye")
def byebye():
    return "<h2>bye :c"

@app.route("/")
def hi():
    return "<h2>Hello!"

@app.route("/hara")
def hara():
    return "<h2>your an hara"

if __name__ == "__main__":
    app.run(debug=True)
