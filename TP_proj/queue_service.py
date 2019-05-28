from db_service import db
from flask import jsonify


class QueueService:
    def __init__(self):
        self.queue = []
        pass

    def form_queue(self, id_user):
        self.queue = []
        #User.create(name="dasha", sex=False, age=23, rating=0, location='', info='student', picture='', login='asa', password='sa')
        couples = db.get_couples(id_user)
        [self.queue.append(sel) for sel in couples]
        #[print(sel) for sel in couples]

    def likes_queue(self, id_user):
        self.queue = []
        likes = db.get_likes(id_user)
        [self.queue.append(sel) for sel in likes]

    def get_from_queue(self):
        if len(self.queue) != 0:
            return self.jsonify_user(self.queue.pop())
        return jsonify(id=0)

    def jsonify_user(self, id_user):
        user = db.get_user(id_user)
        return jsonify(id=user.id,
                       name=user.name,
                       sex=user.sex,
                       age=user.age,
                       rating=user.rating,
                       location=user.location,
                       info=user.login)


queue_service = QueueService()


if __name__ == '__main__':
    service = QueueService()
    service.form_queue(3)
    service.get_from_queue()
