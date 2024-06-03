#!/usr/bin/env python3
""" Module of Basic Authentication
"""

from base64 import b64decode
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(
        self,
        authorization_header: str,
    ) -> str:
        """Extract base64 authorization header"""
        if authorization_header is None or not isinstance(
            authorization_header,
            str,
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the value of a base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode("utf-8")
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode("utf-8")
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str,
    ) -> (str, str):  # type: ignore
        """Extracts user credentials"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        user_pass = decoded_base64_authorization_header.split(":", 1)
        return (user_pass[0], user_pass[1])

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):  # type: ignore
        """User object from credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User()
            user.email = user_email
            user.password = user_pwd
            return user
        except BaseException:
            return None
