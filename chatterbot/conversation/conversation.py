import uuid
from chatterbot.queues import ResponseQueue

class Conversation(ResponseQueue):

    def __init__(self, storage):
        super(Conversation, self).__init__()

        # A unique identifier for the chat session
        # TODO: make these id or pk to match with Django model
        self.uuid = uuid.uuid1()
        self.id_string = str(self.uuid)

        self.storage = storage

    @property
    def statements(self):
        return self.storage.filter(conversation__id=self.id_string)
