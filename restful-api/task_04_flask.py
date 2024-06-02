#!/usr/bin/python3
"""
Set up a Flask application and run a development server.
Define and handle routes with Flask to respond to different endpoints.
Serve JSON data using Flask.
Understand the basics of request handling and response formation in Flask.
Handle POST requests to add new data to the API.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}


@app.route('/')
def home():
    """
    Route for the root URL.
    """

    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Route to get a list of all usernames stored in the API.
    """

    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Route to check the status of the API.
    """

    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Route to get user details by username.
    """

    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Route to add a new user.
    """

    user_data = request.get_json()
    username = user_data.get('username')

    if not username or username in users:
        return jsonify({"error": "Invalid username"}), 400

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == '__main__':
    app.run()
