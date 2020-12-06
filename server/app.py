# === Module Import Statements ===

import json

from flask import Flask, request, jsonify

import DatabaseConnection

import AllergyList
import DatabaseController
import Demographics
import Labwork
import MedicationsList
import Note
from PatientProfile import *

# === Other Class Import Statements ===

# import rooms
# Where we have a .py file named "rooms.py" in the same folder.

# === Global Variables ===

# == Flask ==

app = Flask(__name__)

# == Application ==

# db_controller = DatabaseController.DatabaseController()
db_connection = DatabaseConnection.create_connection()

# === Routes ===

# == Post ==


@app.route('/post/set_medications', methods=['POST'])
def set_medication():
    """
    Writes the provided medication into the database for the patient.
    Input: A JSON containing the following keys
    patientID, id, scientific_name, medicine_name, chemical_name, synonym, suppress
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.set_medication(db_connection, response_dict)
    print_response_json(response)
    return response

# !!! Hey, this is just the same as create_patient(). We're probably never going to make new patients anyway.
# @app.route('/post/set_demographics', methods=['POST'])
# def set_demographics():
#     """
#     Writes the information from the provided Demographics object into the database
#     for the given health_num
#     :param health_num: a 9-digit integer health number corresponding to patient
#     :param demographics: a Demographics object containing patient information
#     """
#     response = request.get_json()
#     response_dict = convert_json_to_dict(response)
#     DatabaseController.set_demographics(db_connection, response_dict)
#     print_response_json(response)
#     return response


@app.route('/post/set_allergies', methods=['POST'])
def set_allergies():
    """
    Writes/Replaces the allergies list into the database for the specified patient
    Input: A JSON containing the following keys
    patientID, item, severity_description, medical_name
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.set_allergies(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/set_lab_work', methods=['POST'])
def set_lab_work():
    """
    Writes the provided Lab work data into the database for the patient
    Input: A JSON containing the following keys
    patientID, testTypeID
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.set_lab_work(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/set_billing', methods=['POST'])
def set_billing():
    """
    Writes the billing information into the database for the given patient
    Input: A JSON containing the following keys
    patientID, medicalSecretaryID, billingCode
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.overwrite_billing(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/append_note', methods=['POST'])
def append_note():
    """
    Append a note to a patients profile in the database
    Input: A JSON containing the following keys
    patientID, author, body
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.insert_note(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/create_patient', methods=['POST'])
def create_patient_profile():
    """
    Add a patient profile to the database.
    Input: A JSON containing the following keys
    federalHealthID, provinceID, name, genderID, dateOfBirth, age, temp, address, familyHistory, medicalConditions
    :return: The JSON that was provided to the POST request to confirm.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.overwrite_patient(db_connection, response_dict)
    print_response_json(response)
    return response


# == Get ==

@app.route('/get/patient/<health_num>', methods=['GET'])
def get_patient(health_num):
    """
    Retrieve patient demographics from the database given their health number.
    :param health_num: patient's health number
    :return: Patient profile JSON
    """
    return DatabaseController.get_patient_demographics(db_connection, health_num)


@app.route('/get/patient_by_id/<patient_id>', methods=['GET'])
def get_patient_by_id(patient_id):
    """
    Retrieve patient demographics from the database given their patient ID.
    :param patient_id: patient's health number
    :return: Patient profile JSON
    """
    return DatabaseController.get_patient_demographics_by_id(db_connection, patient_id)


@app.route('/get/patient_notes/<patient_id>', methods=['GET'])
def get_patient_notes(patient_id):
    """
    Retrieve patient notes from the database given the patientID.
    :param patient_id: patient's health number
    :return: Patient notes JSON
    """
    return DatabaseController.get_patient_notes(db_connection, patient_id)


@app.route('/get/patient_billing/<patient_id>', methods=['GET'])
def get_patient_billing(patient_id):
    """
    Retrieve patient billing from the database given the patientID.
    :param patient_id: patient's health number
    :return: Patient billing JSON
    """
    return DatabaseController.get_billing(db_connection, patient_id)


@app.route('/get/patient_medication/<patient_id>', methods=['GET'])
def get_patient_medication(patient_id):
    """
    Retrieve patient medication from the database given the patientID.
    :param patient_id: patient's health number
    :return: Patient medication JSON
    """
    return DatabaseController.get_medications(db_connection, patient_id)


@app.route('/get/patient_allergies/<patient_id>', methods=['GET'])
def get_patient_allergies(patient_id):
    """
    Retrieve patient allergies from the database given the patientID.
    :param patient_id: patient's health number
    :return: Patient allergies JSON
    """
    return DatabaseController.get_allergies(db_connection, patient_id)


# == Test ==


@app.route('/test/flask_get_test/<get_id>', methods=["GET"])
def flask_get_test(get_id):
    """
    A test URL to see if the server is running GET properly.
    :param get_id: An integer.
    :return: The integer as a string with 42 appended to the end.
    """
    print(get_id)
    return get_id + "42"


@app.route('/test/flask_post_test', methods=["POST"])
def flask_post_test():
    """
    A test URL to see if the server is running POST properly.
    Input: A JSON.
    :return: The JSON received.
    """
    response = request.get_json()
    print_response_json(response)
    return response

# == Flask Helpers ==


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


# === Utility ===


def convert_json_to_dict(json_to_convert):
    json_as_str = json.dumps(json_to_convert)
    json_as_dict = json.loads(json_as_str)
    return json_as_dict


def print_response_json(json_to_print):
    json_as_dict = convert_json_to_dict(json_to_print)
    print(json_as_dict)


# === Main ===


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
