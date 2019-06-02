from db_service import db

class CommentService:
    def __init__(self):
        pass

    def send_comment(self, id_user, id_comment, author, mark, text):
        db.add_comment(id_user, id_comment, author, mark, text)
        db.update_rating(id_comment)
        db.delete_messages(id_user, id_comment)
        db.delete_chat(id_user, id_comment)
        pass


cs = CommentService()
