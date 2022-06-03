from flask import Flask, jsonify, request
from flask_admin import Admin

# Intitialise the appgreet
app = Flask(__name__)

# Define what the app does
@app.get("/")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    name = request.args.get("name")
    if not name:
        response = {"status": "error"}
    else:
        response = {"data": f"Hi {name}!"}

    return jsonify(response)

