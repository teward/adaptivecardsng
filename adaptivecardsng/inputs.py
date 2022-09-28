from __future__ import annotations

from .base import BaseInput, BaseObject
from .enums import TextInputStyle, ChoiceInputStyle

from .actions import Execute, Submit, OpenUrl, ToggleVisibility


class Text(BaseInput):
    def __init__(self,
                 # Objects for Text input specifically
                 id: str, multiline: (bool | None) = None, max_length: (int | None) = None,
                 placeholder: (str | None) = None, regex: (str | None) = None,
                 style: (TextInputStyle | None) = None,
                 inline_action: (Execute | Submit | OpenUrl | ToggleVisibility | None) = None,
                 value: (str | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Text, self).__init__("Input.Text", error_message, required, label,
                                   fallback, height, separator, spacing, visible, requires,
                                   *args, **kwargs)
        self.id = id
        if multiline:
            self.multiline = multiline

        if max_length:
            self.maxLength = max_length

        if placeholder:
            self.placeholder = placeholder

        if regex:
            self.regex = regex

        if style:
            self.style = style

        if inline_action:
            self.inlineAction = inline_action

        if value:
            self.value = value


class Number(BaseInput):
    def __init__(self,
                 # Number items
                 id: str, max: (int | None) = None, min: (int | None) = None,
                 placeholder: (str | None) = None, value: (int | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Number, self).__init__("Input.Number", error_message, required, label,
                                   fallback, height, separator, spacing, visible, requires,
                                   *args, **kwargs)

        self.id = id
        if max:
            self.max = max

        if min:
            self.min = min

        if placeholder:
            self.placeholder = placeholder

        if value:
            self.value = value


class Date(BaseInput):
    def __init__(self,
                 # Date objects
                 id: str, max: (str | None) = None, min: (str | None) = None,
                 placeholder: (str | None) = None, value: (str | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Date, self).__init__("Input.Date", error_message, required, label,
                                   fallback, height, separator, spacing, visible, requires,
                                   *args, **kwargs)
        self.id = id
        if max:
            self.max = max

        if min:
            self.min = min

        if placeholder:
            self.placeholder = placeholder

        if value:
            self.value = value


class Time(BaseInput):
    def __init__(self,
                 # Time objects
                 id: str, max: (str | None) = None, min: (str | None) = None,
                 placeholder: (str | None) = None, value: (str | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Time, self).__init__("Input.Time", error_message, required, label,
                                   fallback, height, separator, spacing, visible, requires,
                                   *args, **kwargs)
        self.id = id
        if max:
            self.max = max

        if min:
            self.min = min

        if placeholder:
            self.placeholder = placeholder

        if value:
            self.value = value


class Toggle(BaseInput):
    def __init__(self,
                 # Toggle items
                 title: str, id: str, value: (bool | None) = None,
                 value_off: (str | None) = None, value_on: (str | None) = None,
                 wrap: (bool | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Toggle, self).__init__("Input.Toggle", error_message, required, label,
                                     fallback, height, separator, spacing, visible, requires,
                                     *args, **kwargs)
        self.title = title
        self.id = id
        if value:
            self.value = value
        if value_off:
            self.value_off = value_off
        if value_on:
            self.value_on = value_on
        if wrap:
            self.wrap = wrap


class Choice(BaseObject):
    def __init__(self, title: str, value: str, *args, **kwargs):
        super(Choice, self).__init__(*args, **kwargs)
        self.title = title
        self.value = value


class ChoiceSet(BaseObject):
    def __init__(self,
                 # Objects for ChoiceSet
                 id: str, choices: (list[Choice] | None) = None,
                 multiselect: (bool | None) = None, style: (ChoiceInputStyle | None) = None,
                 value: (str | None) = None, placeholder: (str | None) = None,
                 wrap: (str | None) = None,
                 # Inherited arguments from SuperClass.
                 error_message: (str | None) = None, required: bool = False,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(ChoiceSet, self).__init__("Input.ChoiceSet", error_message, required, label,
                                        fallback, height, separator, spacing, visible, requires,
                                        *args, **kwargs)
        self.id = id
        if choices:
            self.choices = choices
        if multiselect:
            self.isMultiSelect = multiselect
        if style:
            self.style = style
        if value:
            self.value = value
        if placeholder:
            self.placeholder = placeholder
        if wrap:
            self.wrap = wrap
