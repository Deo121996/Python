import pytest
from main1.basic import get_database_list
class MongoClient:
    def __init__(self, aa, bb):
        pass

    def list_database_names(self):
        return []


def test_get_database_list(mocker):
    client_mock = MongoClient("daas",1212)
    mocker.patch("main1.basic.MongoClient", return_value = client_mock)
    res = get_database_list()
    assert res == False