from db_service import db

class InfoUserService:
    def __init__(self):
        pass

    def add_to_viewed(self, id_viewer, id_viewed):
        db.add_viewed(id_viewer, id_viewed)


inform = InfoUserService()