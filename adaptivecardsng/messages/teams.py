from adaptivecardsng.base import BaseObject
from adaptivecardsng.cards import AdaptiveCard


class TeamsAdaptiveMessage(BaseObject):
    def __init__(self, card: AdaptiveCard):
        super(TeamsAdaptiveMessage, self).__init__()
        self.type = "message"
        self.attachments = [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "contentUrl": None,
            "content": card
        }]
