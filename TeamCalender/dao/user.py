from utils.string_utils import get_random_uuid
from utils.constants import USER_ID_LENGTH

class User:
    def __init__(self):
        self.user_id = get_random_uuid(USER_ID_LENGTH)