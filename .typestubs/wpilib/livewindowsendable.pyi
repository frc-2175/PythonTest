"""
This type stub file was generated by pyright.
"""

from .command.subsystem import Subsystem
from .sendable import Sendable
from .sendablebuilder import SendableBuilder

"""
This type stub file was generated by pyright.
"""
__all__ = ["LiveWindowSendable"]
class LiveWindowSendable(Sendable):
    """A special type of object that can be displayed on the live window.

    .. deprecated:: 2018.0
        Use :class:`.Sendable` directly instead.
    """
    def __init_subclass__(cls, **kwargs) -> None:
        ...
    
    def updateTable(self) -> None:
        """Update the table for this sendable object with the latest
        values.
        """
        ...
    
    def startLiveWindowMode(self) -> None:
        """Start having this sendable object automatically respond to
        value changes reflect the value on the table.

        Default implementation will add self.valueChanged (if it exists)
        as a table listener on "Value".
        """
        ...
    
    def stopLiveWindowMode(self) -> None:
        """Stop having this sendable object automatically respond to value
        changes.
        """
        self.valueListener = ...
    
    def getName(self) -> str:
        ...
    
    def _setName(self, name: str) -> None:
        ...
    
    def getSubsystem(self) -> str:
        ...
    
    def setSubsystem(self, subsystem: Subsystem) -> None:
        ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    


