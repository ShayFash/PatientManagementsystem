import DatabaseConnection
import json as json
import sqlite3


def get_patient_demographics(conn, health_number):
    """
    Returns all demographics information relating to a health number.
    :param conn: Database connection.
    :param health_number: Federal health number of the patient.
    :return: A JSON containing all the information.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient WHERE federalHealthID=?", (health_number,))

    try:
        row = dict(cur.fetchone())
        return row
    except TypeError:
        return False