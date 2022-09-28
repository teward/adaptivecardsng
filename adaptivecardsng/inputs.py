from .base import BaseInput, BaseObject
from .enums import TextInputStyle, ChoiceInputStyle

from .actions import Execute, Submit, OpenUrl, ToggleVisibility

from typing import Optional, Union


class Text(BaseInput):
    def __init__(self,
                 # Objects for Text input specifically
                 id: str, multiline: Optional[bool] = None, max_length: Optional[int] = None,
                 placeholder: Optional[str] = None, regex: Optional[str] = None,
                 style: Optional[TextInputStyle] = None,
                 inline_action: Optional[Union[Execute, Submit, OpenUrl, ToggleVisibility]] = None,
                 value: Optional[str] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 id: str, max: Optional[int] = None, min: Optional[int] = None,
                 placeholder: Optional[str] = None, value: Optional[int] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 id: str, max: Optional[str] = None, min: Optional[str] = None,
                 placeholder: Optional[str] = None, value: Optional[str] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 id: str, max: Optional[str] = None, min: Optional[str] = None,
                 placeholder: Optional[str] = None, value: Optional[str] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 title: str, id: str, value: Optional[bool] = None,
                 value_off: Optional[str] = None, value_on: Optional[str] = None,
                 wrap: Optional[bool] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 id: str, choices: Optional[list[Choice]] = None,
                 multiselect: Optional[bool] = None, style: Optional[ChoiceInputStyle] = None,
                 value: Optional[str] = None, placeholder: Optional[str] = None,
                 wrap: Optional[str] = None,
                 # Inherited arguments from SuperClass.
                 error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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