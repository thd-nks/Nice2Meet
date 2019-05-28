from reviewed_users import reviewed
from info_user_service import inform
from queue_service import queue_service


class RequestHandler:
    def __init__(self):
        pass

    def handle_request(self, is_liked: bool, id_viewer, id_viewed):
        reviewed.set_viewed(id_viewer, id_viewed)
        if is_liked:
            inform.add_to_liked(id_viewer, id_viewed)
        return queue_service.get_from_queue()


request = RequestHandler()