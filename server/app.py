# === Module Import Statements ===

import json
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

# == Get ==

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