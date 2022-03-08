from dao.team import Team
from dao.team_calender import TeamCalender
from dao.meeting import Meeting
from dao.time_slots import TimeSlot
from dao.user import User
team1 = Team()
user1 = User()
user2 = User()
user3 = User()
team1.assign_user_to_team(user1.user_id)
team1.assign_user_to_team(user2.user_id)
team1.assign_user_to_team(user3.user_id)
tc = TeamCalender(team1)

# USER1
meet1 = Meeting("g1u1")
slot1 = TimeSlot(user1.user_id, "11:30", "12:30")

meet2 = Meeting("g2u1")
slot2 = TimeSlot(user1.user_id, "13:30", "14:30")
tc.assign_meeting(meet1, slot1)
tc.assign_meeting(meet2, slot2)


#USER2


meet1 = Meeting("g1u2")
slot1 = TimeSlot(user2.user_id, "14:30", "16:30")

meet2 = Meeting("g2u2")
slot2 = TimeSlot(user2.user_id, "10:30", "11:00")
tc.assign_meeting(meet1, slot1)
tc.assign_meeting(meet2, slot2)


aa = tc.get_todays_meetings()
print("\n\nAll the meetings today")
print(aa)
print("\n\nAll the available slots today")
print(tc.get_available_meeting_slots("fg"))