from flask import Flask
from db_service import DB
from queue_service import QueueService
from chat import Chat
from registration import Registration
from authorization import Authorization
from request_handler import RequestHandler
from reviewed_users import ReviewedUsers
from profile_service import ProfileService
from info_user_service import InfoUserService

app = Flask(__name__)
app.config.from_object('config')


from routes import *


if __name__ == '__main__':
    app.debug = True
    app.run()
