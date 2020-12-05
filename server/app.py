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

# NOTE: The following patient specific methods rely on DatabaseController in which
# I am currently developing, does not exist in this context - Sam


@app.route('/post/set_medications', methods=['POST'])
def set_medications():
    """
    Writes/Replaces the provided medication list into the database for the patient.
    :param health_num: a 9-digit integer health number corresponding to patient
    param medication_list: a MedicationList object
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.set_medications(db_connection, response_dict)
    print_response_json(response)
    return response

# !!! Hey, this is just the same as create_patient()
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
    :param health_num: a 9-digit integer health number corresponding to patient
    :param allergies: an Allergies object already containing allergy information
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
    :param health_num: a 9-digit integer health number corresponding to patient
    :param lab_work: a LabWork object containing the lab work data in question
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
    :param health_num: a patient's health number
    :param billing_code: a String representing patient's billing code.
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.overwrite_billing(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/append_note', methods=['POST'])
def append_note():
    """
    append a note to a patients profile in the database
    :param health_num: the health number of the patient in question
    :param note: a Note object to be inserted
    """
    response = request.get_json()
    response_dict = convert_json_to_dict(response)
    DatabaseController.insert_note(db_connection, response_dict)
    print_response_json(response)
    return response


@app.route('/post/create_patient', methods=['POST'])
def create_patient_profile():
    """
    create a patient profile and pass it on to the database
    :param health_num: patient's health number
    :param full_name: FullName object representing new patient's name
    :param demographics: demographics object containing new patient's demographics
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
    retrieve a patient object from the database given their health number
    :param health_num: patient's health number
    :return: PatientProfile object
    """
    return DatabaseController.get_patient_demographics(db_connection, health_num)

# == Test ==


@app.route('/test/flask_get_test/<get_id>', methods=["GET"])
def flask_get_test(get_id):
    print(get_id)
    return get_id + "42"


@app.route('/test/flask_post_test', methods=["POST"])
def flask_post_test():
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
