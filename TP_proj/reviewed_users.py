from app import db


class ReviewedUsers:
    def __init__(self):
        pass

    def check_viewed(self) -> bool:
        pass

    def set_viewed(self, id_viewer, id_viewed):
        db.add_viewed(id_viewer, id_viewed)
