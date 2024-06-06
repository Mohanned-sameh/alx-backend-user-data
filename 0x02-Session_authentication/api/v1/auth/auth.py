#!/usr/bin/env python3
"""Auth module"""


from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method for validating if endpoint requires auth"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        l_path = len(path)
        if l_path == 0:
            return True

        slash_path = True if path[l_path - 1] == "/" else False

        tmp_path = path
        if not slash_path:
            tmp_path += "/"

        for exc in excluded_paths:
            l_exc = len(exc)
            if l_exc == 0:
                continue

            if exc[l_exc - 1] != "*":
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[: l_exc - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header"""
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):  # type: ignore
        """Current user"""
        return None

    def session_cookie(self, request=None):
        """Session cookie"""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
