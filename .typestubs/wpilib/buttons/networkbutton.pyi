"""
This type stub file was generated by pyright.
"""

from .button import Button
from networktables.networktable import NetworkTable

"""
This type stub file was generated by pyright.
"""
__all__ = ["NetworkButton"]
class NetworkButton(Button):
    """A :class:`.button.Button` that uses a :class:`.NetworkTable` boolean field."""
    def __init__(self, table: NetworkTable, field: str) -> None:
        """Initialize the NetworkButton.

        :param table: the :class:`.NetworkTable` instance to use, or the name of the
                      table to use.
        :param field: field to use.
        """
        ...
    
    def get(self) -> bool:
        """Get the value of the button."""
        ...
    


