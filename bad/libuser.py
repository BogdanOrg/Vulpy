import sqlite3
import libuser


def login(username, password):

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(username, password)).fetchone()

    if user:
        return user['username']
    else:
        return False


#  add comment
def create(username, password):

    conn = sqlite3.connect('db_users.sqlite')
    c = conn.cursor()

    c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')" %(username, password, 0, 0, ''))

    conn.commit()
    conn.close()

def my_func():

    tmp = "my func"

def userlist():

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    users = c.execute("SELECT * FROM users").fetchall()

    if not users:
        return []
    else:
        return [ user['username'] for user in users ]



def password_complexity(password):
    return True

