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


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    login endpoint
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """
    logout endpoint
    """
    session_id = request.cookies.get("session_id")
    email = AUTH.get_user_from_session_id(session_id)
    if email:
        AUTH.destroy_session(email)
        return jsonify({"message": "Bienvenue"})
    else:
        abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """
    profile endpoint
    """
    session_id = request.cookies.get("session_id")
    email = AUTH.get_user_from_session_id(session_id)
    if email:
        return jsonify({"email": email})
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
