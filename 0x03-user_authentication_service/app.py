#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, abort, request, jsonify
import logging
from auth import Auth

AUTH = Auth()
app = Flask(__name__)

logging.disable(logging.WARNING)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    home endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    users endpoint
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
