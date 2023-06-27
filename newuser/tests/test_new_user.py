import os
import time
import unittest

from app.new_user_service import NewUserService
from app.redis_connection import RedisConnection

from dotenv import load_dotenv

load_dotenv()

STREAM_NAME = os.getenv("REDIS_USER_STREAM", "new_user")


class TestNewUser(unittest.TestCase):
    def test_new_user_no_stream(self):
        results = NewUserService().read_stream("0_0")
        self.assertIsNone(results)

    def test_new_user_with_stream(self):
        redis = RedisConnection.get_client()

        user = dict(
            first_name="test_first",
            last_name="test_last",
            email="test_mail@example.com")

        redis.xadd(STREAM_NAME, user)

        print("sleeping")
        time.sleep(2)
        print("awake")

        results = NewUserService().read_stream("0-0")
        entry = results[0][1][0]
        self.assertEqual("test_first", entry[1]["first_name"])
