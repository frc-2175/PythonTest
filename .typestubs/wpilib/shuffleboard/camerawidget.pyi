"""
This type stub file was generated by pyright.
"""

from .container import ShuffleboardContainer
from .widget import ShuffleboardWidget

class CameraWidget(ShuffleboardWidget):
    """A Shuffleboard widget that displays a camera stream from CameraServer.

    Usable via :meth:`.ShuffleboardContainer.addCamera`.
    """
    __slots__ = ...
    kProtocol = ...
    def __init__(self, parent: ShuffleboardContainer, title: str, camera_name: str):
        self.uri = ...
        self.not_created = ...
    
    def buildInto(self, parentTable, metaTable) -> None:
        ...
    


