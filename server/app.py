# === Module Import Statements ===

import json
import PatientProfile, Demographics, Names, Note
from flask import Flask, request, jsonify

# === Other Class Import Statements ===

# import rooms
# Where we have a .py file named "rooms.py" in the same folder.

# === Global Variables ===

# == Flask ==

app = Flask(__name__)

# == Application ==

# === Routes ===

# == Post ==

@app.route('/post/login_user/', methods=["POST"])
def login_user():
    response = request.get_json()
    print_response_json(response)
    
    response_as_dict = convert_json_to_dict(response)
    # user_profile = queries.getUserByUsername(conn, response_as_dict)
    isPasswordValid = passwordHash.verifyPassword(user_profile["password"], json_as_dict["password"])
    print(isPasswordValid)
    
    if (isPasswordValid):
        return jsonify(user_profile["userID"])
        return

    return jsonify("Received post/register_user")

#NOTE: The following four methods rely on DatabaseController in which
#I am currently starting development on, does not exist in this branch/context - Sam

@app.route('/post/set_billing', methods=['POST'])
def set_billing(health_num, billing_code: str):
    """
    :param health_num: a patient's health number
    :param billing_code: a String representing patient's billing code. 
    """
    DatabaseController.overwrite_billing(health_num, billing_code)

@app.route('/post/append_note', methods=['POST'])
def append_note(health_num, note: Note):
    """
    append a note to a patients profile in the database
    :param health_num: the health number of the patient in question
    :param note: a Note object to be inserted
    """
    json_note = json.dumps(note.note)
    DatabaseController.insert_note(health_num, Json_note)

@app.route('/post/create_patient', methods=['POST'])
def create_patient_profile(health_num, full_name: FullName, demographics: Demographics):
    """
    create a patient profile and pass it on to the database
    :param health_num: patient's health number
    :param full_name: FullName object representing new patient's name
    :param demographics: demographics object containing new patient's demographics
    """
    patient = PatientProfile(full_name, demographics)
    DatabaseController.overwrite_patient(health_num, patient)

# == Get ==

@app.route('/get/patient', methods=['GET'])
def get_patient(health_num):
    """
    retrieve a patient object from the database given their health number
    :param health_num: patient's health number
    :return: PatientProfile object
    """
    return DatabaseController.Get_Patient(health_num)
    

@app.route('/get/categories', methods=["GET"])
def get_categories():
    # categories = queries.getCategoriesAsJsons(conn)

    return categories

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