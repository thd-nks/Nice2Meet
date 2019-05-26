from peewee import *

db = MySQLDatabase('nicemeet', user='root', password='root', host='localhost')


class User(Model):
    id = IntegerField(primary_key=True)
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


class Chat(Model):
    idchat = IntegerField(primary_key=True)
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
    db.connect()
    db.create_tables([User, Chat, Message, Comment, LikedUser, ViewedUser])
