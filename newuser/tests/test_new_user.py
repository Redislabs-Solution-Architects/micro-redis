import os
import time

from app.new_user_service import NewUserService
from app.redis_connection import RedisConnection

from dotenv import load_dotenv

load_dotenv()

STREAM_NAME = os.getenv("REDIS_USER_STREAM", "new_user")


def test_new_user_no_stream():
    results = NewUserService().read_stream("0_0")
    assert results is None


def test_new_user_with_stream():
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
    assert entry[1]["first_name"] == "test_first"
