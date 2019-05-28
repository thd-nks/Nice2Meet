from peewee import *
from flask_login import UserMixin
from app import login
from werkzeug.security import generate_password_hash, check_password_hash

db = MySQLDatabase('nicemeet', user='root', password='root', host='localhost')


class User(UserMixin, Model):
    id = AutoField(primary_key=True)
    name = TextField()
    sex = BooleanField()
    age = IntegerField()
    rating = IntegerField()
    location = TextField()
    info = TextField()
    picture = TextField()
    login = TextField()
    password = TextField()

    class Meta:
        db_table = 'user'
        database = db

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login.user_loader
def load_user(id):
    return User.get(User.id == int(id))


class Chat(Model):
    idchat = AutoField(primary_key=True)
    id1 = ForeignKeyField(User, backref='user')
    id2 = ForeignKeyField(User, backref='user')

    class Meta:
        db_table = 'chat'
        database = db
        '''primary_key = CompositeKey('id1', 'id2')'''


class Message(Model):
    idchat = ForeignKeyField(Chat)
    idsender = ForeignKeyField(User)
    date = DateTimeField()
    text = TextField()

    class Meta:
        db_table = 'message'
        database = db
        primary_key = CompositeKey('idchat', 'idsender', 'date')


class Comment(Model):
    iduser = ForeignKeyField(User, backref='user', primary_key=True)
    author = TextField()
    date = DateField()
    mark = IntegerField()
    text = TextField()

    class Meta:
        db_table = 'comment'
        database = db


class LikedUser(Model):
    idliker = ForeignKeyField(User, backref='user')
    idliked = ForeignKeyField(User, backref='user')

    class Meta:
        db_table = 'likeduser'
        database = db
        primary_key = CompositeKey('idliker', 'idliked')


class ViewedUser(Model):
    idviewer = ForeignKeyField(User)
    idviewed = ForeignKeyField(User)

    class Meta:
        db_table = 'vieweduser'
        database = db
        primary_key = CompositeKey('idviewer', 'idviewed')


if __name__ == '__main__':
    #db.connect()
    #db.create_tables([User, Chat, Message, Comment, LikedUser, ViewedUser])
    p = 'root'
    user = User(name="root", sex=True, age=23, rating=0, location='', info='student', picture='', login='asa')
    user.set_password(p)
    user.save()
