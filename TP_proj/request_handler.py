from info_user_service import inform
from db_service import db
from reviewed_users import reviewed

class RequestHandler:
    def __init__(self):
        pass

    def handle_request(self, is_liked, id_viewer, id_viewed):
        if is_liked == '1':
            inform.add_to_viewed(id_viewer, id_viewed)
            db.add_liked(id_viewer, id_viewed)
            query = db.get_likes(id_viewer)
            if query.exists():
                db.add_chat(id_viewer, id_viewed)
        else:
            inform.add_to_viewed(id_viewer, id_viewed)


request = RequestHandler()
