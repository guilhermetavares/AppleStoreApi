import os
from app.models import Application as MongoApplication


def test_starts():
    url = 'https://raw.githubusercontent.com/guilhermetavares/AppleStoreApi/master/tests/BaseTests.csv'
    os.system(f"cd app/ && python start.py {url}")
    assert MongoApplication.objects().first().apple_id == '281656475'
