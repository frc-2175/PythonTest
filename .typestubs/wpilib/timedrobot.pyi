"""
This type stub file was generated by pyright.
"""

from typing import Optional
from .iterativerobotbase import IterativeRobotBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["TimedRobot"]
class TimedRobot(IterativeRobotBase):
    """TimedRobot implements the IterativeRobotBase robot program framework.

    The TimedRobot class is intended to be subclassed by a user creating a robot program.

    periodic() functions from the base class are called on an interval by a Notifier instance.
    """
    kDefaultPeriod = ...
    def __init__(self, period: Optional[float] = ...) -> None:
        ...
    
    def free(self) -> None:
        ...
    
    def startCompetition(self) -> None:
        """Provide an alternate "main loop" via startCompetition()"""
        ...
    
    def getPeriod(self) -> float:
        """Get time period between calls to Periodic() functions."""
        ...
    
    def _updateAlarm(self) -> None:
        """Update the alarm hardware to reflect the next alarm."""
        ...
    


