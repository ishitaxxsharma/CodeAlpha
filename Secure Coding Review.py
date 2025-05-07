# Insecure code
def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pwd='{password}'"
    print("Running query:", query)

# Secure version using parameterized queries
import sqlite3
def secure_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name=? AND pwd=?", (username, password))
    print("User authenticated:", cursor.fetchone())
