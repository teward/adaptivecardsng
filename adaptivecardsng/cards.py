from __future__ import annotations

from .base import BaseObject, BaseElement, BaseAction
from .actions import Execute, OpenUrl, Submit, ToggleVisibility
from .types import Refresh, Authentication, BackgroundImage
from .enums import VerticalAlignment


class AdaptiveCard(BaseObject):
    """
    The base Adaptive Card object that holds elements, containers, etc.

    Inherits from BaseObject.

    See Also
        BaseObject
    """
    def __init__(self, refresh: (Refresh | None) = None,
                 authentication: (Authentication | None) = None,
                 body: (list[BaseObject] | None) = None,
                 actions: (BaseAction | None) = None,
                 select_action: (Execute | OpenUrl | Submit | ToggleVisibility | None) = None,
                 fallback_text: (str | None) = None,
                 background_image: (BackgroundImage | str | None) = None,
                 min_height: (str | None) = None, rtl: (bool | None) = None,
                 speak: (str | None) = None, lang: (str | None) = None,
                 vertical_content_alignment: (VerticalAlignment | None) = None,
                 *args, **kwargs):
        super(AdaptiveCard, self).__init__(*args, **kwargs)
        # type, version and $schema are hardcoded
        self.type = "AdaptiveCard"
        self.version = "1.5"
        # We shouldn't be touching symbols definitions in __dict__, but we have an odd
        # symbol-required object, so we'll fudge the rules a little just for this one.
        # While $schema is an optional item, we provide it as static.
        self.__dict__['$schema'] = 'https://adaptivecards.io/schemas/adaptive-card.json'

        if refresh:
            self.refresh = refresh
        if authentication:
            self.authentication = authentication
        if body:
            self.body = body
        if actions:
            self.actions = actions
        if select_action:
            self.selectAction = select_action
        if fallback_text:
            self.fallbackText = fallback_text
        if background_image:
            self.backgroundImage = background_image
        if min_height:
            self.minHeight = min_height
        if rtl:
            self.rtl = rtl
        if speak:
            self.speak = speak
        if lang:
            self.lang = lang
        if vertical_content_alignment:
            self.verticalContentAlignment = vertical_content_alignment
