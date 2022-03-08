from concurrent.futures import ThreadPoolExecutor
from utils.string_utils import get_random_uuid
from utils.time_utils import get_date_params_today, get_date_time_object_from_time, get_string_time_stamp
from utils.constants import TEAM_CALENDER_ID, TEAM_CALENDER_ID_LENGTH, MEETING_ID, \
    USER_ID, START_TIME, END_TIME, GUEST_ID, FROM, TO
from dao.team import Team
from dao.time_slots import TimeSlot
from dao.meeting import Meeting

class TeamCalender:
    def __init__(self, team: Team):
        self.calender_id = get_random_uuid(TEAM_CALENDER_ID_LENGTH)
        self.team = team
        self.meeting_map = dict()

    def initialise_todays_meeting_map(self):
        year, month, day = get_date_params_today()
        if not self.meeting_map.get(year):
            self.meeting_map[year] = dict()

        if not self.meeting_map[year].get(month):
            self.meeting_map[year][month] = dict()

        if not self.meeting_map[year][month].get(day):
            self.meeting_map[year][month][day] = dict()

        return year, month, day

    def assign_meeting(self, meeting: Meeting, slot: TimeSlot):
        year, month, day = self.initialise_todays_meeting_map()
        if not self.meeting_map[year][month][day].get(slot.user_id):
            self.meeting_map[year][month][day][slot.user_id] = list()

        meeting.start_time = get_date_time_object_from_time(slot.from_time)
        meeting.end_time = get_date_time_object_from_time(slot.to_time)
        self.meeting_map[year][month][day][slot.user_id].append(meeting)
        return meeting.meeting_id

    def get_todays_meetings(self):
        year, month, day = self.initialise_todays_meeting_map()
        result = dict()
        all_meetings = list()
        for user, meetings in self.meeting_map[year][month][day].items():
            for meeting_obj in meetings:
                meeting = dict()
                meeting[USER_ID] = user
                meeting[MEETING_ID] = meeting_obj.meeting_id
                meeting[START_TIME] = get_string_time_stamp(meeting_obj.start_time)
                meeting[END_TIME] = get_string_time_stamp(meeting_obj.end_time)
                meeting[GUEST_ID] = meeting_obj.guest_id
                all_meetings.append(meeting)
        result[TEAM_CALENDER_ID] = self.calender_id
        result["meetings"] = sorted(all_meetings, key=lambda slot: slot[START_TIME])
        return result

    def get_user_time_slots(self, user_id):
        year, month, day = self.initialise_todays_meeting_map()
        time_slot_list = list()
        user_meetings = self.meeting_map[year][month][day].get(user_id, {})
        if user_meetings:
            schedule = { meeting.start_time: meeting.end_time for meeting in user_meetings}
            start_schedule = sorted(schedule.keys())
            end_schedule = sorted(schedule.values())
            time_slot = dict()
            time_slot[FROM] = get_date_time_object_from_time("00:00")
            time_slot[TO] = start_schedule[0]
            time_slot[USER_ID] = user_id
            time_slot_list.append(time_slot)

            for i in range(len(start_schedule)-1):
                if (start_schedule[i+1] - end_schedule[i]).seconds >= 30:
                    time_slot = dict()
                    time_slot[FROM] = end_schedule[i]
                    time_slot[TO] = start_schedule[i+1]
                    time_slot[USER_ID] = user_id
                    time_slot_list.append(time_slot)
            time_slot = dict()
            time_slot[FROM] = end_schedule[-1]
            time_slot[TO] = get_date_time_object_from_time("00:00", add_time_delta=1)
            time_slot[USER_ID] = user_id
            time_slot_list.append(time_slot)
        else:
            time_slot = dict()
            time_slot[FROM] = get_date_time_object_from_time("00:00")
            time_slot[TO] = get_date_time_object_from_time("00:00", add_time_delta=1)
            time_slot[USER_ID] = user_id
            time_slot_list.append(time_slot)

        return time_slot_list

    def get_time_stamps_for_all_users(self):
        users_list = self.team.users_list
        with ThreadPoolExecutor(max_workers=5) as executor:
            result = executor.map(lambda x : self.get_user_time_slots(*x), list(zip(users_list)))
        return result
    

    def get_slots_by_fastest_algo(self):
        result = self.get_time_stamps_for_all_users()
        final = []
        [final.extend(slot) for slot in result]
        return sorted(final, key=lambda slot: slot[FROM])

    def get_slots_by_round_robin_algo(self):
        result = self.get_time_stamps_for_all_users()
        result = [record for record in result]
        result = sorted(result, key=lambda x: len(x))
        final = []
        [final.extend(slot) for slot in result]
        return final

    def get_available_meeting_slots(self, algo="fastest"):
        result = dict()
        slots = None
        if algo == "fastest":
            slots = self.get_slots_by_fastest_algo()
        else:
            slots = self.get_slots_by_round_robin_algo()
        return self.massage_slots_response(slots)

    @staticmethod
    def massage_slots_response(slots):
        for slot in slots:
            slot[FROM] = get_string_time_stamp(slot[FROM])
            slot[TO] = get_string_time_stamp(slot[TO]) if slot.get(TO) else None

        return slots
