from db.database import query_user
from utils.crypto import verify_password

def authenticate(username, password):
    user = query_user(username)
    if not user:
        return "Invalid user", 401

    if verify_password(password, user["password_hash"]):
        return "Login successful"
    return "Invalid credentials", 403
