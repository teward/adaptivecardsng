from .base import BaseElement, BaseObject

from .enums import Colors, FontType, HorizontalAlignment
from .enums import FontSize, FontWeight, TextBlockStyle
from .enums import BlockElementHeight, Spacing, ImageSize
from .enums import ImageStyle

from .actions import Execute, OpenUrl, Submit, ToggleVisibility

from typing import Optional, List, Union


class TextBlock(BaseElement):
    def __init__(self,
                 # Items from TextBlock
                 text: str, color: Optional[Colors] = None, font_type: Optional[FontType] = None,
                 horizontal_alignment: Optional[HorizontalAlignment] = None,
                 subtle: Optional[bool] = None, max_lines: Optional[int] = None,
                 font_size: Optional[FontSize] = None,
                 font_weight: Optional[FontWeight] = None,
                 wrap: Optional[bool] = None,
                 style: Union[str, TextBlockStyle] = TextBlockStyle.default,
                 # Inherited from BaseElement - except "type" which is hardcoded in
                 # super call.
                 fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None, visible: bool = True,
                 id: Optional[str] = None, requires: Optional[dict] = None,
                 *args, **kwargs) -> None:

        super().__init__("TextBlock", fallback, height, separator, spacing,
                         visible, id, requires, *args, **kwargs)
        self.text = text
        if color:
            self.color = color
        if font_type:
            self.fontType = font_type
        if horizontal_alignment:
            self.horizontalAlignment = horizontal_alignment
        if subtle:
            self.isSubtle = subtle
        if max_lines:
            self.maxLines = max_lines
        if font_size:
            self.size = font_size
        if font_weight:
            self.weight = font_weight
        if wrap:
            self.wrap = wrap
        if style:
            self.style = style


class Image(BaseElement):
    def __init__(self,
                 # Items from Image
                 url: str, alt_text: Optional[str] = None,
                 background_color: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 horizontal_alignment: Optional[HorizontalAlignment] = None,
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 size: Optional[ImageSize] = None, style: Optional[ImageStyle] = None,
                 width: Optional[str] = None,
                 # Inherited from BaseElement - except "type" which is hardcoded in
                 # super call.
                 fallback: Optional[str] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None, visible: bool = True,
                 id: Optional[str] = None, requires: Optional[dict] = None,
                 *args, **kwargs) -> None:
        super().__init__("Image", fallback, height, separator, spacing,
                         visible, id, requires, *args, **kwargs)
        if url:
            self.url = url
        if alt_text:
            self.altText = alt_text
        if background_color:
            self.backgroundColor = background_color
        if height and height not in ['auto', BlockElementHeight.auto]:
            self.height = height
        if horizontal_alignment:
            self.horizontalAlignment = horizontal_alignment
        if select_action:
            self.selectAction = select_action
        if size:
            self.size = size
        if style:
            self.style = style


class MediaSource(BaseObject):
    def __init__(self, url: str, mime_type: Optional[str] = None, *args, **kwargs):
        super(MediaSource, self).__init__(*args, **kwargs)
        self.url = url

        # This is to enforce the requirement that a data: URI defines the MIMEType.
        if self.url.startswith('data:') and not mime_type:
            raise ValueError("If you are defining a data URI, you must define the MIMEType "
                             "of the data.")

        if self.url.startswith('data:') and mime_type:
            self.mimeType = mime_type

        if not self.url.startswith('data:') and mime_type:
            self.mimeType = mime_type


class Media(BaseElement):
    def __init__(self,
                 # Items from Media
                 sources: List[MediaSource], poster: Optional[str] = None,
                 alt_text: Optional[str] = None,
                 # Inherited from BaseElement - except "type" which is hardcoded in
                 # super call.
                 fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None, visible: bool = True,
                 id: Optional[str] = None, requires: Optional[dict] = None,
                 *args, **kwargs) -> None:
        super(Media, self).__init__("Media", fallback, height, separator, spacing, visible,
                                    id, requires, *args, **kwargs)
        self.sources = sources
        if poster:
            self.poster = poster
        if alt_text:
            self.altText = alt_text


class TextRun(BaseObject):
    def __init__(self, text: str, color: Optional[Colors] = None,
                 font_type: Optional[FontType] = None, highlight: Optional[bool] = None,
                 subtle: Optional[bool] = None, italic: Optional[bool] = None,
                 select_action: Optional[Union[Execute, OpenUrl, Submit, ToggleVisibility]] = None,
                 size: Optional[FontSize] = None, strikethrough: Optional[bool] = None,
                 underline: Optional[bool] = None, weight: Optional[FontWeight] = None,
                 *args, **kwargs):
        super(TextRun, self).__init__(*args, **kwargs)
        self.text = text
        if color:
            self.color = color
        if font_type:
            self.fontType = font_type
        if highlight:
            self.highlight = highlight
        if subtle:
            self.isSubtle = subtle
        if italic:
            self.italic = italic
        if select_action:
            self.selectAction = select_action
        if size:
            self.size = size
        if strikethrough:
            self.strikethrough = strikethrough
        if underline:
            self.underline = underline
        if weight:
            self.weight = weight


class RichTextBlock(BaseElement):
    def __init__(self,
                 # Items from RichTextBlock
                 inlines: list[Union[str, TextRun]],
                 horizontal_alignment: Optional[HorizontalAlignment] = None,
                 # Inherited from BaseElement - except "type" which is hardcoded in
                 # super call.
                 fallback: Optional[str] = None,
                 height: Optional[Union[str, BlockElementHeight]] = None,
                 separator: Optional[bool] = None,
                 spacing: Optional[Union[str, Spacing]] = None, visible: bool = True,
                 id: Optional[str] = None, requires: Optional[dict] = None,
                 *args, **kwargs) -> None:
        super(RichTextBlock, self).__init__("RichTextBlock", fallback, height, separator, spacing,
                                            visible, id, requires, *args, **kwargs)
        self.inlines = inlines
        if horizontal_alignment:
            self.horizontalAlignment = horizontal_alignment