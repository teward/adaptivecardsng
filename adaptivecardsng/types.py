from __future__ import annotations

from .base import BaseObject
from .enums import ImageFillMode, HorizontalAlignment, VerticalAlignment

from .actions import Execute


# Types are object definitions which can be used in many places -
# containers, elements, inputs, etc. and have mutable options
# as part of their definitions and initialization.
#
# Because of this, where it makes sense to do so, we declare
# certain object types here instead of elsewhere in the
# code base.
#
# These differ from Enums, because they have mutable values.
# Enums are completely static definitions.

class BackgroundImage(BaseObject):
    def __init__(self, url: str, fill_mode: (ImageFillMode | None) = None,
                 horizontal_alignment: (HorizontalAlignment | None) = None,
                 vertical_alignment: (VerticalAlignment | None) = None,
                 *args, **kwargs) -> None:
        super(BackgroundImage, self).__init__(*args, **kwargs)
        self.url = url

        if fill_mode:
            self.fillMode = fill_mode

        if horizontal_alignment:
            self.horizontalAlignment = horizontal_alignment

        if vertical_alignment:
            self.verticalAlignment = vertical_alignment


class Refresh(BaseObject):
    def __init__(self, execute: (Execute | None) = None,
                 user_ids: (dict[str] | None) = None,
                 *args, **kwargs) -> None:
        super(Refresh, self).__init__(*args, **kwargs)
        if execute:
            self.execute = execute

        if user_ids:
            self.userIds = user_ids


class TokenExchangeResource(BaseObject):
    def __init__(self, id: str, uri: str, provider_id: str, *args, **kwargs):
        super(TokenExchangeResource, self).__init__(*args, **kwargs)
        self.id = id
        self.uri = uri
        self.providerId = provider_id


class AuthCardButton(BaseObject):
    def __init__(self, type: str, value: str, title: (str | None) = None,
                 image: (str | None) = None, *args, **kwargs):
        super(AuthCardButton, self).__init__(*args, **kwargs)
        self.type = type
        self.value = value
        if title:
            self.title = title

        if image:
            self.image = image


class Authentication(BaseObject):
    def __init__(self, text: (str | None) = None, connection_name: (str | None) = None,
                 token_exchange_resource: (TokenExchangeResource | None) = None,
                 buttons: (list[AuthCardButton] | None) = None, *args, **kwargs) -> None:
        super(Authentication, self).__init__(*args, **kwargs)
        if text:
            self.text = text

        if connection_name:
            self.connectionName = connection_name

        if token_exchange_resource:
            self.tokenExchangeResource = token_exchange_resource

        if buttons:
            self.buttons = buttons
