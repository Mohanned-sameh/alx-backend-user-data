#!/usr/bin/env python3
"""
Module for handling Personal Data
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
