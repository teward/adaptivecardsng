from __future__ import annotations

import json
import enum

from .enums import BlockElementHeight, Spacing, ActionStyle, ActionMode


class BaseObjectJSONEncoder(json.JSONEncoder):
    """Specialized JSON Encoder for adaptivecardsng BaseObject and its subclasses."""
    def default(self, obj: BaseObject):
        """
        Default JSON handler function for generating JSON data.

        Args:
            obj (BaseObject): Any BaseObject or subclassed objects.

        Returns:

        """
        if isinstance(obj, enum.Enum):
            return str(obj.value)

        return obj.__dict__


class BaseObject:
    """
    Custom base object class for all other objects and classes in the project.

    Designed so that it's designed to properly work with the object's own dictionary
    for symbols declarations where needed.
    """
    def __init__(self, *args, **kwargs) -> None:
        self.__dict__.update(*args, **kwargs)

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key) -> object:
        return self.__dict__[key]

    def __delitem__(self, key) -> None:
        del self.__dict__[key]

    def __iter__(self) -> iter:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, indent=2, cls=BaseObjectJSONEncoder)

    def __repr__(self):
        return self.__str__()

    def insert(self, key, value):
        if key not in self.__dict__.keys():
            self.__setitem__(key, value)
        else:
            raise ValueError("Specified key already exists.")

    def as_json(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, indent=2,
                          separators=(',', ':'), cls=BaseObjectJSONEncoder)


class BaseElement(BaseObject):
    """
    Base class for Element type objects, used in elements.py and its classes.

    Inherits from BaseObject.

    See Also:
        BaseObject
    """
    def __init__(self, element_type: (str | None) = None, fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None,
                 spacing: (str | Spacing | None) = None, visible: (bool | None) = None,
                 id: (str | None) = None, requires: (dict | None) = None,
                 *args, **kwargs):
        """
        Args:
            element_type (str, optional):
            fallback (str, optional):
            height (str/BlockElementHeight, optional):
            separator (bool, optional):
            spacing (str/Spacing, optional):
            visible (bool, optional):
            id (str, optional):
            requires (dict, optional):
        """
        super().__init__(*args, **kwargs)
        if element_type:
            self.type = element_type
        if fallback:
            self.fallback = fallback
        if height:
            self.height = height
        if separator and separator is True:
            self.separator = separator
        if spacing:
            self.spacing = spacing
        if visible and visible is False:
            self.isVisible = visible
        if id:
            self.id = id
        if requires:
            self.requires = requires


class BaseAction(BaseObject):
    """
    Base class for Action type objects, used in actions.py and its classes.

    Inherits from BaseObject.

    See Also:
        BaseObject
    """
    def __init__(self, action_type: str, title: (str | None) = None,
                 icon_url: (str | None) = None,
                 id: (str | None) = None, style: (str | ActionStyle | None) = None,
                 fallback: (str | None) = None, tooltip: (str | None) = None,
                 enabled: (bool | None) = None, mode: (str | ActionMode | None) = None,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        """
        Args:
            action_type (str):
            title (str, optional_:
            icon_url (str, optional):
            id (str, optional):
            style (str/ActionStyle, optional):
            fallback (str, optional):
            tooltip (str, optional):
            enabled (bool, optional):
            mode (str/ActionMode, optional):
            requires (dict, optional):
        """
        super().__init__(*args, **kwargs)
        self.type = action_type
        if title:
            self.title = title
        if icon_url:
            self.iconUrl = icon_url
        if id:
            self.id = id
        if style:
            self.style = style
        if fallback:
            self.fallback = fallback
        if tooltip:
            self.tooltip = tooltip
        if enabled and enabled is False:
            self.isEnabled = enabled
        if mode and mode not in ['primary', ActionMode.primary]:
            self.mode = mode
        if requires:
            self.requires = requires


class BaseInput(BaseObject):
    """
    Base class for Input type objects, used in inputs.py and its classes.

    Inherits from BaseObject.

    See Also:
        BaseObject
    """
    def __init__(self, input_type: str, error_message: (str | None) = None,
                 required: (bool | None) = None,
                 label: (str | None) = None, fallback: (str | None) = None,
                 height: (str | None) = None, separator: (bool | None) = False,
                 spacing: (str | None) = None, visible: (bool | None) = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        """

        Args:
            input_type (str):
            error_message (str, optional):
            required (bool, optional):
            label (str, optional):
            fallback (str, optional):
            height (str, optional):
            separator (bool, optional):
            spacing (str, optional):
            visible (bool, optional):
            requires (dict, optional):
        """
        super().__init__(*args, **kwargs)

        self.type = input_type
        if error_message:
            self.errorMessage = error_message
        if required:
            self.isRequired = required
        if label:
            self.label = label
        if fallback:
            self.fallback = fallback
        if height:
            self.height = height
        if separator:
            self.separator = separator
        if spacing:
            self.spacing = spacing
        if visible and visible is False:
            self.isVisible = visible
        if requires:
            self.requires = requires


class BaseContainer(BaseObject):
    """
    Base class for Container type objects, used in containers.py and its classes.

    Inherits from BaseObject.

    See Also:
        BaseObject
    """
    def __init__(self, container_type: str, fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = False,
                 spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: (bool | None) = None,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        """
        Args:
            container_type (str):
            fallback (str, optional):
            height (str / BlockElementHeight, optional):
            separator (bool, optional):
            spacing (str / Spacing, optional):
            id (str, optional):
            visible (bool, optional):
            requires (dict, optional):
        """
        super().__init__(*args, **kwargs)
        self.type = container_type
        if fallback:
            self.fallback = fallback
        if height:
            self.height = height
        if separator:
            self.separator = separator
        if spacing:
            self.spacing = spacing
        if id:
            self.id = id
        if visible and visible is False:
            self.isVisible = visible
        if requires:
            self.requires = requires


class BaseSet(BaseObject):
    """
    Base class for Set type objects, used in various classes and definitions.

    Inherits from BaseObject.

    See Also:
        BaseObject
    """
    def __init__(self, set_type: str, fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None,
                 spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: (bool | None) = None,
                 requires: (dict | None) = None, *args, **kwargs):
        """
        Args:
            set_type (str):
            fallback (str, optional):
            height (str / BlockElementHeight, optional):
            separator (bool, optional):
            spacing (str / Spacing, optional):
            id (str, optional):
            visible (bool, optional):
            requires (dict, optional):
        """
        super(BaseSet, self).__init__(*args, **kwargs)
        self.type = set_type
        if fallback:
            self.fallback = fallback
        if height:
            self.height = height
        if separator:
            self.separator = separator
        if spacing:
            self.spacing = spacing
        if id:
            self.id = id
        if visible and visible is False:
            self.isVisible = visible
        if requires:
            self.requires = requires
