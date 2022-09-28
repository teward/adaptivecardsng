import enum

# There are a number of functions and definitions which define
# statically defined Enums in the system.  Where it makes sense
# for such enums to exist (and be reused in many locations),
# those Enums we encounter are defined in here.
#
# This may be an unusual approach, but it's actually a good one
# since these enums are used in NUMEROUS object types ranging
# from elements to containers to inputs even to specific types.
#
# What makes this different from Types is that Types are
# object definitions with mutable definitions for the
# arguments, etc. and do not contain constants.
#
# Enums contain only constants that won't change, hence they are
# defined separately here.


class FontType(enum.Enum):
    default = "default"
    monospace = "monospace"


class FontSize(enum.Enum):
    default = "default"
    small = "small"
    medium = "medium"
    large = "large"
    extra_large = "extraLarge"


class FontWeight(enum.Enum):
    default = "default"
    lighter = "lighter"
    bolder = "bolder"


class TextBlockStyle(enum.Enum):
    default = "default"
    heading = "heading"


class ImageFillMode(enum.Enum):
    cover = "cover"
    repeat_horizontally = "repeatHorizontally"
    repeat_vertically = "repeatVertically"
    repeat = "repeat"


class ImageSize(enum.Enum):
    auto = "auto"
    stretch = "stretch"
    small = "small"
    medium = "medium"
    large = "large"


class ImageStyle(enum.Enum):
    default = "default"
    person = "person"


class HorizontalAlignment(enum.Enum):
    left = "left"
    center = "center"
    right = "right"


class VerticalAlignment(enum.Enum):
    top = "top"
    center = "center"
    bottom = "bottom"


class BlockElementHeight(enum.Enum):
    auto = "auto"
    stretch = "stretch"


class Spacing(enum.Enum):
    default = "default"
    none = "none"
    small = "small"
    medium = "medium"
    large = "large"
    extra_large = "extraLarge"
    padding = "padding"


class ActionStyle(enum.Enum):
    default = "default"
    positive = "positive"
    destructive = "destructive"


class ActionMode(enum.Enum):
    primary = "primary"
    secondary = "secondary"


class AssociatedInputs(enum.Enum):
    auto = "auto"
    none = "none"


class Colors(enum.Enum):
    default = "default"
    dark = "dark"
    light = "light"
    accent = "accent"
    good = "good"
    warning = "warning"
    attention = "attention"


class ContainerStyle(enum.Enum):
    default = "default"
    emphasis = "emphasis"
    good = "good"
    attention = "attention"
    warning = "warning"
    accent = "accent"


class TextInputStyle(enum.Enum):
    text = "text"
    tel = "tel"
    url = "url"
    email = "email"
    password = "password"


class ChoiceInputStyle(enum.Enum):
    compact = "compact"
    expanded = "expanded"
    filtered = "filtered"
