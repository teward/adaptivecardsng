import json
import enum

from .enums import BlockElementHeight, Spacing, ActionStyle, ActionMode


class BaseObjectJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return str(obj.value)

        return obj.__dict__


class BaseObject:
    def __init__(self, *args, **kwargs) -> None:
        self.__dict__.update(*args, **kwargs)

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key) -> object:
        return self.__dict__[key]

    def __delitem__(self, key) -> None:
        del self.__dict__[key]

    def __iter__(self) -> Iterable:
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
        return json.dumps(self.__dict__, indent=2, cls=BaseObjectJSONEncoder)


class BaseElement(BaseObject):
    def __init__(self, element_type: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None, visible: bool = True,
                 id: Optional[str] = None, requires: Optional[dict] = None,
                 *args, **kwargs):
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
    def __init__(self, action_type: str, title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
    def __init__(self, input_type: str, error_message: Optional[str] = None, required: bool = False,
                 label: Optional[str] = None, fallback: Optional[str] = None,
                 height: Optional[str] = None, separator: Optional[bool] = False,
                 spacing: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
    def __init__(self, container_type: str, fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = False,
                 spacing: Optional[Union[str, Spacing]] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
    def __init__(self, set_type: str, fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs):
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
