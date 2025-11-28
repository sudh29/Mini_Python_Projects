import flask as flask

app = flask.Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/<name>")
def hello_name(name):
    return name.capitalize()


if __name__ == "__main__":
    app.run()
