
from utils.string_utils import get_random_uuid
from utils.constants import TEAM_ID_LENGTH

class Team:
    def __init__(self):
        self.team_id = get_random_uuid(TEAM_ID_LENGTH)
        self.users_list = list()
    
    def get_all_user_ids(self):
        return self.users_list
    
    def assign_user_to_team(self, user_id):
        self.users_list.append(user_id)
