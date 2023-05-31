import hashlib

from app.utility import redis_conn


def validate_identity(email, password):
    user = redis_conn.json().get(f"users:{email}")
    pass_hash = hashlib.md5(password.encode()).hexdigest()
    if pass_hash != user["password"]:
        return False
    else:
        return True
