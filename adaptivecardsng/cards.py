from .base import BaseObject


class AdaptiveCard(BaseObject):
    def __init__(self, background_image: str = None, vertical_content_alignment: str = None,
                 select_action: str = None, min_height: str = None, fallback_text: str = None,
                 body: list = None, actions: list = None, speak: str = None, lang: str = None,
                 *args, **kwargs):
        super(AdaptiveCard, self).__init__(*args, **kwargs)
        # type, version and $schema are hardcoded
        self.type = "AdaptiveCard"
        self.version = "1.5"
        # We shouldn't be touching symbols definitions in __dict__, but we have an odd
        # symbol-required object, so we'll fudge the rules a little just for this one.
        # While $schema is an optional item, we provide it as static.
        self.__dict__['$schema'] = 'https://adaptivecards.io/schemas/adaptive-card.json'

        # the remaining arguments are mutable (and optional) via init.
        if background_image:
            self.backgroundImage = background_image
        if vertical_content_alignment:
            self.verticalContentAlignment = vertical_content_alignment
        if select_action:
            self.selectAction = select_action
        if min_height:
            self.minHeight = min_height
        if fallback_text:
            self.fallbackText = fallback_text
        if body:
            self.body = body
        if actions:
            self.actions = actions
        if speak:
            self.speak = speak
        if lang:
            self.lang = lang