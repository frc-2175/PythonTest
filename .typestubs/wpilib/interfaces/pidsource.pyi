"""
This type stub file was generated by pyright.
"""

import enum
from typing import Callable

"""
This type stub file was generated by pyright.
"""
__all__ = ["PIDSource"]
class PIDSource:
    """This interface allows for :class:`.PIDController` to automatically read from this
    object.
    """
    @staticmethod
    def from_obj_or_callable(objc: PIDSource) -> PIDSource:
        """
            Utility method that gets a PIDSource object
        
            :param objc: An object that implements the PIDSource interface, or
                         a callable
                         
            :returns: an object that implements the PIDSource interface 
        """
        ...
    
    class PIDSourceType(enum.IntEnum):
        """A description for the type of output value to provide to a
        :class:`.PIDController`"""
        kDisplacement = ...
        kRate = ...
    
    
    def setPIDSourceType(self, pidSource: PIDSourceType) -> None:
        """Set which parameter of the device you are using as a process control
        variable.
        
        :param pidSource: An enum to select the parameter.
        """
        ...
    
    def getPIDSourceType(self) -> PIDSourceType:
        """Get which parameter of the device you are using as a process control
           variable.
           
        :returns: the currently selected PID source parameter
        """
        ...
    
    def pidGet(self) -> float:
        """Get the result to use in :class:`.PIDController`
        
        :returns: the result to use in PIDController
        """
        ...
    


class _PIDSourceWrapper(PIDSource):
    def __init__(self, fn: Callable) -> None:
        self.pidGet = ...
    
    def getPIDSourceType(self) -> PIDSource.PIDSourceType:
        ...
    


