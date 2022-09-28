from .base import BaseAction, BaseSet, BaseContainer, BaseElement, BaseObject

from .enums import BlockElementHeight, Spacing, ContainerStyle
from .enums import VerticalAlignment, HorizontalAlignment, ImageSize

from .elements import Image

from .actions import Execute, OpenUrl, Submit, ToggleVisibility

from .types import BackgroundImage

from typing import Optional, List, Iterable, Union


class ActionSet(BaseSet):
    def __init__(self,
                 # ActionSet Items
                 actions: List[BaseAction],
                 # Inherited from BaseSet
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = None, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
        super(ActionSet, self).__init__("ActionSet", fallback, height, separator, spacing, id,
                                        visible, requires, *args, **kwargs)
        self.actions = actions


class Container(BaseContainer):
    def __init__(self,
                 # Container Items
                 items: List[BaseElement],
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 style: Optional[ContainerStyle] = None,
                 vertical_content_alignment: Optional[VerticalAlignment] = None,
                 bleed: Optional[bool] = None,
                 background_image: Optional[BackgroundImage] = None,
                 min_height: Optional[str] = None, rtl: Optional[bool] = None,
                 # Inherited from BaseContainer
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = None, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
    def __init__(self, items: Optional[List[BaseElement]] = None,
                 background_image: Optional[str, BackgroundImage] = None,
                 bleed: Optional[bool] = None, fallback: Optional[str] = None,
                 min_height: Optional[str] = None, rtl: Optional[bool] = None,
                 separator: Optional[bool] = None, spacing: Optional[Spacing] = None,
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 style: Optional[ContainerStyle] = None,
                 vertical_content_alignment: Optional[VerticalAlignment] = None,
                 width: Optional[int, str] = None,
                 # Note: this SHOULD be part of a base class but doesn't fit into
                 # any current base objects.  So, we have defined this as its own object.
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 columns: Optional[List[Column]] = None,
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 style: Optional[ContainerStyle] = None,
                 bleed: Optional[bool] = None,
                 min_height: Optional[str] = None,
                 horizontal_alignment: Optional[HorizontalAlignment] = None,
                 # Inherited from BaseSet
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = None, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
                 facts: List[Fact],
                 # Inherited Items
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = None, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
        super(FactSet, self).__init__("FactSet", fallback, height, separator, spacing, id,
                                      visible, requires, *args, **kwargs)
        self.facts = facts


class ImageSet(BaseSet):
    def __init__(self,
                 # ImageSet Items
                 images: List[Image], image_size: Optional[ImageSize] = None,
                 # Inherited Items
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = None, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
        super(ImageSet, self).__init__("ImageSet", fallback, height, separator, spacing, id,
                                       visible, requires, *args, **kwargs)
        self.images = images
        if image_size:
            self.imageSize = image_size


class TableCell(BaseContainer):
    def __init__(self, items: List[BaseElement],
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 style: Optional[ContainerStyle] = None,
                 vertical_content_alignment: Optional[VerticalAlignment] = None,
                 bleed: Optional[bool] = None,
                 background_image: Optional[str, BackgroundImage] = None,
                 min_height: Optional[str] = None,
                 rtl: Optional[bool] = None, *args, **kwargs):
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
    def __init__(self, cells: Optional[List[TableCell]] = None,
                 style: Optional[ContainerStyle] = None,
                 horizontal_cell_content_alignment: Optional[HorizontalAlignment] = None,
                 vertical_cell_content_alignment: Optional[VerticalAlignment] = None,
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
                 columns: Optional[Iterable] = None,
                 rows: Optional[TableRow] = None,
                 first_row_as_header: Optional[bool] = None,
                 show_grid_lines: Optional[bool] = None,
                 grid_style: Optional[ContainerStyle] = None,
                 horizontal_cell_content_alignment: Optional[HorizontalAlignment] = None,
                 vertical_cell_content_alignment: Optional[VerticalAlignment] = None,
                 # Inherited from BaseContainer
                 fallback: Optional[str] = None,
                 height: Optional[str, BlockElementHeight] = None,
                 separator: Optional[bool] = False, spacing: Optional[str, Spacing] = None,
                 id: Optional[str] = None, visible: bool = True,
                 requires: Optional[dict] = None, *args, **kwargs) -> None:
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
