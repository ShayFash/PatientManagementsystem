import DatabaseConnection
import json as json
import sqlite3


# == Read ==


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


def get_patient_demographics_by_id(conn, patient_id):
    """
    Returns all demographics information relating to a patientID.
    :param conn: Database connection.
    :param patient_id: PatientID number of the patient.
    :return: A JSON containing all the information.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient WHERE patientID=?", (patient_id,))

    try:
        row = dict(cur.fetchone())
        return row
    except TypeError:
        return False


def get_patient_notes(conn, patient_id):
    """
    Returns all notes relating to a patient_id
    :param conn: Database connection.
    :param patient_id: PatientID number of the patient.
    :return: A JSON containing all the notes.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Note WHERE patientID=?", (patient_id,))

    rows = [dict(row) for row in cur.fetchall()]
    json_rows = json.dumps(rows)
    return json_rows


def get_billing(conn, patient_id):
    """
    Returns all billing relating to a patient_id
    :param conn: Database connection.
    :param patient_id: PatientID number of the patient.
    :return: A JSON containing all the billing.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Billing WHERE patientID=?", (patient_id,))

    rows = [dict(row) for row in cur.fetchall()]
    json_rows = json.dumps(rows)
    return json_rows


def get_medications(conn, patient_id):
    """
    Returns all medication relating to the patient_id
    :param conn: Database connection.
    :param patient_id: PatientID number of the patient.
    :return: A JSON containing all the medication.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM MedicationEntry WHERE patientID=?", (patient_id,))

    rows = [dict(row) for row in cur.fetchall()]
    json_rows = json.dumps(rows)
    return json_rows


def get_allergies(conn, patient_id):
    """
    Returns all allergies relating to the patient_id
    :param conn: Database connection.
    :param patient_id: PatientID number of the patient.
    :return: A JSON containing all the medication.
    """
    conn.row_factory = DatabaseConnection.sq.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM Allergies WHERE patientID=?", (patient_id,))

    rows = [dict(row) for row in cur.fetchall()]
    print(rows)
    json_rows = json.dumps(rows)
    return json_rows

# == Write ==


def overwrite_patient(conn, response_dict):
    """
    
    """
    patient_sql = (response_dict["federalHealthID"], response_dict["provinceID"], response_dict["name"],
                   response_dict["genderID"], response_dict["dateOfBirth"], response_dict["age"],
                   response_dict["temp"], response_dict["address"], response_dict["familyHistory"],
                   response_dict["medicalConditions"])
    sql = '''   INSERT OR REPLACE INTO Patient(federalHealthID, provinceID, name, genderID, dateOfBirth, age, temp, address, familyHistory, medicalConditions)
                VALUES(?,?,?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, patient_sql)
    conn.commit()


def insert_note(conn, response_dict):
    """

    """
    note_sql = (response_dict["patientID"], response_dict["author"], response_dict["body"])
    sql = '''   INSERT INTO Note(patientID, date, author, body)
                VALUES(?,date('now'),?,?)'''
    cur = conn.cursor()
    cur.execute(sql, note_sql)
    conn.commit()


def overwrite_billing(conn, response_dict):
    """

    """
    billing_sql = (response_dict["patientID"], response_dict["medicalSecretaryID"], response_dict["billingCode"])
    sql = '''   INSERT INTO Billing(patientID, datetime, medicalSecretaryID, billingCode)
                VALUES(?,datetime('now'),?,?)'''
    cur = conn.cursor()
    cur.execute(sql, billing_sql)
    conn.commit()


def set_lab_work(conn, response_dict):
    """

    """
    lab_work_sql = (response_dict["patientID"], response_dict["testTypeID"])
    sql = '''   INSERT INTO LabTest(patientID, testTypeID)
                VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql, lab_work_sql)
    conn.commit()


def set_allergies(conn, response_dict):
    """

    """
    allergies_sql = (response_dict["patientID"], response_dict["item"], response_dict["severity_description"],
                     response_dict["medical_name"])
    sql = '''   INSERT INTO Allergies(patientID, item, severity_description, medical_name)
                VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, allergies_sql)
    conn.commit()


def set_medication(conn, response_dict):
    """

    """
    medication_sql = (response_dict["patientID"], response_dict["id"], response_dict["scientific_name"],
                      response_dict["medicine_name"], response_dict["chemical_name"], response_dict["synonym"],
                      response_dict["suppress"])
    sql = '''   INSERT INTO MedicationEntry(patientID, id, scientific_name, medicine_name, chemical_name, synonym, suppress)
                VALUES(?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, medication_sql)
    conn.commit()
