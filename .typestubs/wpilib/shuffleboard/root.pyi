"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING
from .tab import ShuffleboardTab

"""
This type stub file was generated by pyright.
"""
if TYPE_CHECKING:
    ...
class ShuffleboardRoot:
    """
    The root of the data placed in Shuffleboard. It contains the tabs, but no 
    data is placed directly in the root.
    """
    def getTab(self, title: str) -> ShuffleboardTab:
        """
        Gets the tab with the given title, creating it if it does not 
        already exist.

        :param title: the title of the tab
        :returns: the tab with the given title
        """
        ...
    
    def update(self) -> None:
        """Updates all tabs."""
        ...
    
    def enableActuatorWidgets(self) -> None:
        """Enables all widgets in Shuffleboard that offer user control over actuators."""
        ...
    
    def disableActuatorWidgets(self) -> None:
        """Disables all widgets in Shuffleboard that offer user control over actuators."""
        ...
    
    def selectTab(self, index_or_title) -> None:
        """
        Selects the tab in the dashboard with the given index in the 
        range [0..n-1], where `n` is the number of tabs in the dashboard at 
        the time this method is called.

        Or

        Selects the tab in the dashboard with the given title.

        :param index_or_title: when integer, the index of the tab to select.
                               when string, the title of the tab to select.
        """
        ...
    


