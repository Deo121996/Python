import datetime
from utils.constants import DATE_TIME_FORMAT


def get_string_time_stamp(time_stamp=None):
    if not time_stamp:
        time_stamp = datetime.datetime.now()
    todays_string_time_stamp = time_stamp.strftime(DATE_TIME_FORMAT)
    return todays_string_time_stamp


def get_date_time_object_from_time(string_time, add_time_delta=None):

    if len(string_time) < 16:
        time_now = get_string_time_stamp()
        date_params = time_now.split(" ")
        string_time_stamp = " ".join([date_params[0], string_time])
    datetime_object = datetime.datetime.strptime(string_time_stamp, DATE_TIME_FORMAT)
    if add_time_delta:
        datetime_object += datetime.timedelta(days=add_time_delta)

    return datetime_object

def get_date_params_today():
    todays_string_time_stamp = get_string_time_stamp()
    ymd_string = todays_string_time_stamp.split(" ")[0]
    ymd_list = ymd_string.split("-")
    return ymd_list[0], ymd_list[1], ymd_list[2]
