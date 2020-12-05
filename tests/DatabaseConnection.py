import sqlite3 as sq
from sqlite3 import Error
import os.path


def create_connection():
    """ create a database connection to a SQLite database """
    db_connection = None
    try:
        db_connection = sq.connect(os.path.abspath("../db/medical.db"), check_same_thread=False)
        print(sq.version)
    except Error as e:
        print(e)

    return db_connection


if __name__ == "__main__":
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient")

    rows = cur.fetchall()

    for row in rows:
        print(row)

# EOF
