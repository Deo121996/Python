import math
from random import choice
from string import ascii_uppercase


def get_random_uuid(string_length=12):
    return ''.join(choice(ascii_uppercase) for i in range(string_length))


def get_rounded_value(val):
    return math.ceil(val*100.0)/100.0
