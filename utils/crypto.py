import hashlib

def verify_password(password, stored_hash):
    return hashlib.md5(password.encode()).hexdigest() == stored_hash
