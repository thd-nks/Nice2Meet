from flask import Flask
import chat
from authorization import Authorization

app = Flask(__name__)


@app.route("/")
def hello():
    return "Nice to meet you!"


if __name__ == '__main__':
    app.debug = True
    app.run()
