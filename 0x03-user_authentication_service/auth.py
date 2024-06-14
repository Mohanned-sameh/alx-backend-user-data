#!/usr/bin/env python3
"""
auth file
"""
from db import DB
import bcrypt
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth Class"""

    def __init__(self):
        """Constructor"""
        self.db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user"""
        try:
            self.db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self.db.add_user(email, _hash_password(password))
