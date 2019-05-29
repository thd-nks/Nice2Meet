from models import *


class DB:
    def __init__(self):
        pass

    def get_user(self, id_user):
        return User.get_by_id(id_user)

    def get_couples(self, id_user):
        user = User.get_by_id(id_user)
        viewed = ViewedUser.select(ViewedUser.idviewed).where(ViewedUser.idviewer == id_user)
        return User.select(User.id).where(User.age.between(user.age-2, user.age+2),
                                          User.sex != user.sex,
                                          User.location == user.location,
                                          User.id.not_in(viewed))

    def get_likes(self, id_user):
        return LikedUser.select(LikedUser.idliker).where(LikedUser.idliked == id_user)

    def get_chat(self, id_user, id_talk):
        return Chat.select().where(Chat.id1 == id_user & Chat.id2 == id_talk | Chat.id2 == id_user & Chat.id1 == id_talk)

    def add_viewed(self, id_viewer, id_viewed):
        ViewedUser.create(idviewer=id_viewer, idviewed=id_viewed)

    def update_user(self, id):
        pass

db = DB()