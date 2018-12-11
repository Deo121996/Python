import pytest
from flask import Flask

from main1.final import SessionDAO
app = Flask(__name__)

input = {
    "id":1,
    "presentor":"omkar",
    "session":"Python"

}
output = {
    "id":1,
    "presentor":"omkar",
    "session":"Python",
    "extra":"extra"

}


def test_create():
    obj = SessionDAO()
    result = obj.create(input, 1)
    assert result == output

@pytest.mark.parametrize("input1,output1,id",
[(input,output,1),
(None,None,1)
])
def test_get(input1,output1,id):
    obj = SessionDAO()
    obj.create(input1)
    result = obj.get(id)
    assert result == output1