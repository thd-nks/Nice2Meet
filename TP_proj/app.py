from flask import Flask
from chat import Chat
from authorization import Authorization
from request_handler import RequestHandler

app = Flask(__name__)


@app.route("/")
def hello():
    return "Nice to meet you!"


if __name__ == '__main__':
    app.debug = True
    app.run()
