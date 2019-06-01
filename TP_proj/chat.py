from db_service import db


class Chat:
    def __init__(self):
        self.id = 0

    def send_message(self, id_user, id_talk, msg):
        db.send_message(id_user, id_talk, msg)
        return True

    def get_chat(self, id_user, id_talk):
        return db.get_chat(id_user, id_talk)

    def get_messages(self, id_user, id_talk):
        id = db.get_chat(id_user, id_talk)
        msg = db.get_messages(id[0], id_user, id_talk)
        d = [(str(m.idsender_id), str(m.text)) for m in msg]
        return d

    def get_talks(self, id_user):
        temp = db.get_talk(id_user)
        return [(db.get_name(t.id1_id), t.id1_id) if t.id2_id == id_user else
                (db.get_name(t.id2_id), t.id2_id) for t in temp]


ch = Chat()

if __name__ == '__main__':
    ch = Chat()
    ch.get_messages(2, 3)
