import sys
from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1> RODO PoC builder under: </h1><p>Python: {ver}</p>".format(ver=sys.version)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)