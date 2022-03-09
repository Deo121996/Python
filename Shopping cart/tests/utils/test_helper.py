from utils.helper import get_random_uuid, get_rounded_value

def test_get_random_uuid():
    random_id = get_random_uuid(12)
    assert len(random_id) == 12

def test_get_rounded_value():
    assert get_rounded_value(314.9555) == 314.96

