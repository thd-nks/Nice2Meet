from flask import Flask
from db_service import DB
from queue_service import QueueService
from chat import Chat
from registration import Registration
from authorization import Authorization
from request_handler import RequestHandler
from reviewed_users import ReviewedUsers
from profile_service import ProfileService

app = Flask(__name__)


@app.route("/")
def hello():
    return "Nice to meet you!"


if __name__ == '__main__':
    app.debug = True
    app.run()
