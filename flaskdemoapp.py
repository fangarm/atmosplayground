import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "This is data magic"

app.run()
