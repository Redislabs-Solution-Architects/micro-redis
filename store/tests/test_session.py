import unittest

from flask import request
from werkzeug.http import dump_cookie

from app import app
from app.utility import redis_conn
from app.utility import session

app.testing = True
client = app.test_client()


class TestSession(unittest.TestCase):
    def test_create_session(self):
        session_id = session.create_session("bob@example.com")
        self.assertIsNotNone(session_id)

    def test_get_session(self):
        session_id = session.create_session("bob@example.com")

        with app.test_request_context(environ_base={}):
            the_session = session.get_session(request)
            self.assertIsNone(the_session)

        header = dump_cookie("storesessionid", session_id)
        with app.test_request_context(environ_base={'HTTP_COOKIE': header}):
            cookie = request.cookies["storesessionid"]
            self.assertEqual(session_id, cookie)
            the_session = session.get_session(request)
            self.assertEqual("bob@example.com", the_session)

    def test_delete_session(self):
        session_id = session.create_session("bob@example.com")
        self.assertIsNotNone(session_id)
        the_session = redis_conn.get(f"sessions:{session_id}")
        self.assertIsNotNone(the_session)
        session.delete_session(session_id)
        deleted_session = redis_conn.get(f"sessions:{session_id}")
        self.assertIsNone(deleted_session)
