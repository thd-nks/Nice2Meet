from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


from routes import *


if __name__ == '__main__':
    app.debug = True
    app.run()
