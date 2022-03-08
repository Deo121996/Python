from utils.string_utils import get_random_uuid

def test_get_random_uuid():
    random_id = get_random_uuid(12)
    assert len(random_id) == 12
