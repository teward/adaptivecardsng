import sys
if (3, 7) <= sys.version_info < (3, 9):
    from __future__ import annotations

from .base import BaseAction, BaseObject
from .cards import AdaptiveCard
from .enums import ActionStyle, ActionMode, AssociatedInputs

from typing import Optional, Union, List


class OpenUrl(BaseAction):
    def __init__(self,
                 # OpenURL items
                 url: str,
                 # BaseAction Inherited
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs):
        super(OpenUrl, self).__init__("Action.OpenURL", title, icon_url, id, style,
                                      fallback, tooltip, enabled, mode, requires,
                                      *args, **kwargs)
        self.url = url


class Submit(BaseAction):
    def __init__(self,
                 # Submit items
                 data: Optional[Union[str, object]] = None,
                 associated_inputs: Optional[AssociatedInputs] = AssociatedInputs.auto,
                 # BaseAction Inherited
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs):
        super(Submit, self).__init__("Action.Submit", title, icon_url, id, style,
                                      fallback, tooltip, enabled, mode, requires,
                                      *args, **kwargs)
        if data:
            self.data = data

        if associated_inputs and associated_inputs is not AssociatedInputs.auto:
            self.associatedInputs = associated_inputs


class ShowCard(BaseAction):
    def __init__(self,
                 # ShowCard items
                 card: Optional[AdaptiveCard] = None,
                 # BaseAction Inherited
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs):
        super(ShowCard, self).__init__("Action.ShowCard", title, icon_url, id, style,
                                       fallback, tooltip, enabled, mode, requires,
                                       *args, **kwargs)
        if card:
            self.card = card


class TargetElement(BaseObject):
    def __init__(self, element_id: str, visible: Optional[bool] = None, *args, **kwargs):
        super(TargetElement, self).__init__(*args, **kwargs)
        self.elementId = element_id
        if visible:
            self.isVisisble = visible


class ToggleVisibility(BaseAction):
    def __init__(self,
                 # ToggleVisibility items
                 target_elements: list[TargetElement],
                 # BaseAction Inherited
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs):
        super(ToggleVisibility, self).__init__(
            "Action.ToggleVisibility", title, icon_url, id, style,
            fallback, tooltip, enabled, mode, requires,
            *args, **kwargs)
        self.targetElements = target_elements


class Execute(BaseAction):
    def __init__(self,
                 # Execute items
                 verb: Optional[str] = None,
                 data: Optional[Union[str, object]] = None,
                 associated_inputs: Optional[AssociatedInputs] = None,
                 # BaseAction Inherited
                 title: Optional[str] = None,
                 icon_url: Optional[str] = None,
                 id: Optional[str] = None, style: Optional[Union[str, ActionStyle]] = None,
                 fallback: Optional[str] = None, tooltip: Optional[str] = None,
                 enabled: bool = True, mode: Optional[Union[str, ActionMode]] = None,
                 requires: Optional[dict] = None, *args, **kwargs):
        super(Execute, self).__init__(
            "Action.Execute", title, icon_url, id, style,
            fallback, tooltip, enabled, mode, requires,
            *args, **kwargs)
        if verb:
            self.verb = verb
        if data:
            self.data = data
        if associated_inputs:
            self.associatedInputs = associated_inputs