from chatterbot.conversation import Conversation
from chatterbot.conversation.session import SessionManager
from .base_case import ChatBotTestCase


class SessionTestCase(ChatBotTestCase):

    def test_id_string(self):
        conversation = Conversation(self.chatbot.storage)
        self.assertEqual(str(conversation.uuid), conversation.id_string)

class SessionManagerTestCase(ChatBotTestCase):

    def setUp(self):
        super(SessionManagerTestCase, self).setUp()
        self.manager = SessionManager(self.chatbot.storage)

    def test_new(self):
        session = self.manager.new()

        self.assertTrue(isinstance(session, Conversation))
        self.assertIn(session.id_string, self.manager.sessions)
        self.assertEqual(session, self.manager.sessions[session.id_string])

    def test_get(self):
        session = self.manager.new()
        returned_session = self.manager.get(session.id_string)

        self.assertEqual(session.id_string, returned_session.id_string)

    def test_get_invalid_id(self):
        returned_session = self.manager.get('--invalid--')

        self.assertIsNone(returned_session)

    def test_get_invalid_id_with_deafult(self):
        returned_session = self.manager.get('--invalid--', 'default_value')

        self.assertEqual(returned_session, 'default_value')

    def test_update(self):
        session = self.manager.new()
        self.manager.update(session.id_string, ('A', 'B', ))

        session_ids = list(self.manager.sessions.keys())
        session_id = session_ids[0]

        self.assertEqual(len(session_ids), 1)
        self.assertEqual(len(self.manager.get(session_id).conversation), 1)
        self.assertEqual(('A', 'B', ), self.manager.get(session_id).conversation[0])

    def test_get_default(self):
        session = self.manager.new()
        returned_session = self.manager.get_default()

        self.assertEqual(session.id_string, returned_session.id_string)

    def test_update_default(self):
        self.manager.new()
        self.manager.update_default(('A', 'B', ))

        self.assertEqual(len(self.manager.sessions.keys()), 1)
        self.assertEqual(len(self.manager.get_default().conversation), 1)
        self.assertEqual(('A', 'B', ), self.manager.get_default().conversation[0])
