#!/usr/bin/env python3
"""Session Authentication"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication Class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID"""
        if user_id is None or type(user_id) is not str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def destroy_session(self, request=None) -> bool:
        """Destroy a session ID"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
