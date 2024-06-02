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
    Root endpoint that returns a welcome message.
    """

    return "Welcome to the Flask API!"


@app.route('/data')
def json_data():
    """
    Endpoint that returns a JSON list of usernames.
    """

    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """
    Endpoint that returns a simple status message to indicate the server is running.
    """

    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to retrieve data for a specific user by username.
    """

    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=["POST"])
def add_user():
    """
    Endpoint to add a new user via a POST request.
    """

    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
