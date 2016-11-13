

# TODO: Rename to ConversationSessionManager
class SessionManager(object):
    """
    Object to hold and manage multiple chat sessions.
    """

    def __init__(self, storage):
        self.storage = storage
        self.sessions = {}

    def new(self):
        """
        Add a new chat session.
        """
        session = self.storage.create_conversation()

        self.sessions[session.id_string] = session

        return session

    def get(self, session_id, default=None):
        """
        Return a session given a unique identifier.
        """
        return self.sessions.get(str(session_id), default)

    def update(self, session_id, conversance):
        """
        Add a conversance to a given session if the session exists.
        """
        session_id = str(session_id)
        if session_id in self.sessions:
            self.sessions[session_id].conversation.append(conversance)

    def get_default(self):
        """
        Return the first and preferably only session.
        """
        if not self.sessions:
            return None

        session_id = list(self.sessions.keys())[0]
        return self.sessions[session_id]

    def update_default(self, conversance):
        """
        Add a conversance to the first and preferably only session.
        """
        if self.sessions:
            session_id = list(self.sessions.keys())[0]
            self.sessions[session_id].conversation.append(conversance)
