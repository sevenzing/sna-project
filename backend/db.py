import sqlite3
import typing


DATABASE = 'database.db'


def get_conn():
    return sqlite3.connect(DATABASE)


DB_NAME = 'urls'

print('creating schema')
conn = get_conn()
try:
    conn.execute(f'''CREATE TABLE {DB_NAME} (initial_url TEXT, key TEXT)''')
except sqlite3.OperationalError as e:
    print(e)
print('done.')

conn.close()


def put_url(key: str, url: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {DB_NAME} VALUES (?, ?)", (url, key))
    conn.commit()
    conn.close()


def get_url(key: str) -> typing.Optional[str]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"select initial_url from {DB_NAME} where key=:key", {"key": key})
    res = cur.fetchall()
    conn.close()
    if res:
        return res[0][0]
