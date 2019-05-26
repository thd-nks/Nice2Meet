from reviewed_users import ReviewedUsers
from models import *
from db_service import DB

db = DB()


class QueueService:
    def __init__(self):
        self.queue = []
        pass

    def form_queue(self, id_user):
        #User.create(name="Никита", sex=True, age=24, rating=0, location='', info='student', picture='', login='sasa', password='sa')
        self.queue = db.get_couples(id_user)
        [print(sel) for sel in self.queue]
        return self.queue


if __name__ == '__main__':
    service = QueueService()
    service.form_queue(1)
