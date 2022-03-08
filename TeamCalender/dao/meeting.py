from utils.string_utils import get_random_uuid
from utils.constants import MEETING_ID_LENGTH

class Meeting:
    def __init__(self, guest_id):
        self.meeting_id = get_random_uuid(MEETING_ID_LENGTH)
        self.guest_id = guest_id
        self.start_time = None
        self.end_time = None
