import sqlite3

def query_user(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()

    sql = f"SELECT username, password_hash FROM users WHERE username = '{username}'"
    cur.execute(sql)

    row = cur.fetchone()
    if not row:
        return None

    return {"username": row[0], "password_hash": row[1]}
