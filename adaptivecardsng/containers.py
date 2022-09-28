from __future__ import annotations

from .base import BaseAction, BaseSet, BaseContainer, BaseElement, BaseObject

from .enums import BlockElementHeight, Spacing, ContainerStyle
from .enums import VerticalAlignment, HorizontalAlignment, ImageSize

from .elements import Image

from .actions import Execute, OpenUrl, Submit, ToggleVisibility

from .types import BackgroundImage


class ActionSet(BaseSet):
    def __init__(self,
                 # ActionSet Items
                 actions: list[BaseAction],
                 # Inherited from BaseSet
                 fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None, spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(ActionSet, self).__init__("ActionSet", fallback, height, separator, spacing, id,
                                        visible, requires, *args, **kwargs)
        self.actions = actions


class Container(BaseContainer):
    def __init__(self,
                 # Container Items
                 items: list[BaseElement],
                 select_action: (Execute | OpenUrl | Submit | ToggleVisibility | None) = None,
                 style: (ContainerStyle | None) = None,
                 vertical_content_alignment: (VerticalAlignment | None) = None,
                 bleed: (bool | None) = None,
                 background_image: (BackgroundImage | None) = None,
                 min_height: (str | None) = None, rtl: (bool | None) = None,
                 # Inherited from BaseContainer
                 fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None, spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Container, self).__init__("Container", fallback, height, separator, spacing, id,
                                        visible, requires, *args, **kwargs)
        self.items = items
        if select_action:
            self.selectAction = select_action
        if style:
            self.style = style
        if vertical_content_alignment:
            self.verticalContentAlignment = vertical_content_alignment
        if bleed:
            self.bleed = bleed
        if background_image:
            self.backgroundIMage = background_image
        if min_height:
            self.minHeight = min_height
        if rtl:
            self.__dict__['rtl?'] = rtl


class Column(BaseObject):
    def __init__(self, items: (list[BaseElement] | None) = None,
                 background_image: (str | BackgroundImage | None) = None,
                 bleed: (bool | None) = None, fallback: (str | None) = None,
                 min_height: (str | None) = None, rtl: (bool | None) = None,
                 separator: (bool | None) = None, spacing: (Spacing | None) = None,
                 select_action: (Execute | OpenUrl | Submit | ToggleVisibility | None) = None,
                 style: (ContainerStyle | None) = None,
                 vertical_content_alignment: (VerticalAlignment | None) = None,
                 width: (int | str | None) = None,
                 # Note: this SHOULD be part of a base class but doesn't fit into
                 # any current base objects.  So, we have defined this as its own object.
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Column, self).__init__(*args, **kwargs)
        if items:
            self.items = items
        if background_image:
            self.backgroundImage = background_image
        if bleed:
            self.bleed = bleed
        if fallback:
            self.fallback = fallback
        if min_height:
            self.minHeight = min_height
        if rtl:
            self.rtl = rtl
        if separator:
            self.separator = separator
        if spacing:
            self.spacing = spacing
        if select_action:
            self.selectAction = select_action
        if style:
            self.style = style
        if vertical_content_alignment:
            self.verticalContentAlignment = vertical_content_alignment
        if width:
            self.width = width
        if id:
            self.id = id
        if visible and visible is False:
            self.isVisible = visible
        if requires:
            self.requires = requires


class ColumnSet(BaseSet):
    def __init__(self,
                 # ColumnSet Items
                 columns: (list[Column] | None) = None,
                 select_action: (Execute | OpenUrl | Submit | ToggleVisibility | None) = None,
                 style: (ContainerStyle | None) = None,
                 bleed: (bool | None) = None,
                 min_height: (str | None) = None,
                 horizontal_alignment: (HorizontalAlignment | None) = None,
                 # Inherited from BaseSet
                 fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None, spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(ColumnSet, self).__init__("ColumnSet", fallback, height, separator, spacing, id,
                                        visible, requires, *args, **kwargs)
        if columns:
            self.columns = columns
        if select_action:
            self.selectAction = select_action
        if style:
            self.style = style
        if bleed:
            self.bleed = bleed
        if min_height:
            self.minHeight = min_height
        if horizontal_alignment:
            self.horizontalAlignment = horizontal_alignment


class Fact(BaseObject):
    def __init__(self, title: str, value: str, *args, **kwargs):
        super(Fact, self).__init__(*args, **kwargs)
        self.title = title
        self.value = value


class FactSet(BaseSet):
    def __init__(self,
                 # FactSet Items
                 facts: list[Fact],
                 # Inherited Items
                 fallback: (str | None) = None,
                 height: (str, BlockElementHeight | None) = None,
                 separator: (bool | None) = None, spacing: (str, Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(FactSet, self).__init__("FactSet", fallback, height, separator, spacing, id,
                                      visible, requires, *args, **kwargs)
        self.facts = facts


class ImageSet(BaseSet):
    def __init__(self,
                 # ImageSet Items
                 images: list[Image], image_size: (ImageSize | None) = None,
                 # Inherited Items
                 fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = None, spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(ImageSet, self).__init__("ImageSet", fallback, height, separator, spacing, id,
                                       visible, requires, *args, **kwargs)
        self.images = images
        if image_size:
            self.imageSize = image_size


class TableCell(BaseContainer):
    def __init__(self, items: list[BaseElement],
                 select_action: (Execute | OpenUrl | Submit | ToggleVisibility | None) = None,
                 style: (ContainerStyle | None) = None,
                 vertical_content_alignment: (VerticalAlignment | None) = None,
                 bleed: (bool | None) = None,
                 background_image: (str | BackgroundImage | None) = None,
                 min_height: (str | None) = None,
                 rtl: (bool | None) = None, *args, **kwargs):
        super(TableCell, self).__init__(*args, **kwargs)
        self.items = items
        if select_action:
            self.selectAction = select_action
        if style:
            self.style = style
        if vertical_content_alignment:
            self.verticalContentAlignment = vertical_content_alignment
        if bleed:
            self.bleed = bleed
        if background_image:
            self.backgroundImage = background_image
        if min_height:
            self.minHeight = min_height
        if rtl:
            self.__dict__['rtl?'] = rtl


class TableRow(BaseObject):
    def __init__(self, cells: (list[TableCell] | None) = None,
                 style: (ContainerStyle | None) = None,
                 horizontal_cell_content_alignment: (HorizontalAlignment | None) = None,
                 vertical_cell_content_alignment: (VerticalAlignment | None) = None,
                 *args, **kwargs):
        super(TableRow, self).__init__(*args, **kwargs)
        self.type = 'TableRow'
        if cells:
            self.cells = cells
        if style:
            self.style = style
        if horizontal_cell_content_alignment:
            self.horizontalCellContentAlignment = horizontal_cell_content_alignment
        if vertical_cell_content_alignment:
            self.verticalCellContentAlignment = vertical_cell_content_alignment


class Table(BaseContainer):
    def __init__(self,
                 # Table specific items
                 columns: (list | dict | None) = None,
                 rows: (TableRow | None) = None,
                 first_row_as_header: (bool | None) = None,
                 show_grid_lines: (bool | None) = None,
                 grid_style: (ContainerStyle | None) = None,
                 horizontal_cell_content_alignment: (HorizontalAlignment | None) = None,
                 vertical_cell_content_alignment: (VerticalAlignment | None) = None,
                 # Inherited from BaseContainer
                 fallback: (str | None) = None,
                 height: (str | BlockElementHeight | None) = None,
                 separator: (bool | None) = False, spacing: (str | Spacing | None) = None,
                 id: (str | None) = None, visible: bool = True,
                 requires: (dict | None) = None, *args, **kwargs) -> None:
        super(Table, self).__init__("Container", fallback, height, separator, spacing, id,
                                    visible, requires, *args, **kwargs)
        if columns:
            self.columns = columns
        if rows:
            self.rows = rows
        if first_row_as_header:
            self.firstRowAsHeader = first_row_as_header
        if show_grid_lines:
            self.showGridLines = show_grid_lines
        if grid_style:
            self.gridStyle = grid_style
        if horizontal_cell_content_alignment:
            self.horizontalCellContentAlignment = horizontal_cell_content_alignment
        if vertical_cell_content_alignment:
            self.verticalCellContentAlignment = vertical_cell_content_alignment
