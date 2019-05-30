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

    def get_user_by_login(self, login):
        try:
            return User.get(User.login == login)
        except User.DoesNotExist:
            return None

    def update_location(self, id, new_location):
        user = User.get(User.id == id)
        user.location = new_location
        user.save()

    def update_profile(self, id, new_name, new_age, new_info):
        user = User.get(User.id == id)
        user.name = new_name
        user.age = new_age
        user.info = new_info
        user.save()

    def get_likes(self, id_user):
        return LikedUser.select(LikedUser.idliker).where(LikedUser.idliked == id_user)

    def add_viewed(self, id_viewer, id_viewed):
        ViewedUser.create(idviewer=id_viewer, idviewed=id_viewed)

    def update_user(self, id):
        pass

    def get_chat(self, id1, id2):
        pass


db = DB()