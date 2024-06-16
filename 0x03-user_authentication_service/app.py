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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
