#!/usr/bin/env python3
"""
Define class SessionDButh
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Definition of SessionDBAuth class that persists session data
    in a database
    """

    def create_session(self, user_id=None):
        """
        Creates a new session for a user
        Args:
            user_id (str): user id
        """
        if not user_id:
            return None
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        UserSession(user_id=user_id, session_id=session_id).save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a User ID based on a Session ID
        Args:
            session_id (str): session id
        """
        if not session_id:
            return None
        user = UserSession.search({"session_id": session_id})
        if not user:
            return None
        user = user[0]
        return user.user_id

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout
        Args:
            request (obj): request object
        """
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        UserSession.delete(user_id)
        return True
