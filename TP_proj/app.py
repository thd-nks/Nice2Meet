from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login = LoginManager(app)

from routes import *


if __name__ == '__main__':
    app.debug = True
    app.run()
