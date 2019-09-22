"""
This type stub file was generated by pyright.
"""

from .sendablebase import SendableBase
from .sendablebuilder import SendableBuilder

"""
This type stub file was generated by pyright.
"""
__all__ = ["GyroBase"]
class GyroBase(SendableBase):
    """
        GyroBase is the common base class for Gyro implementations such as
        :class:`.AnalogGyro`.
    """
    PIDSourceType = ...
    def __init__(self) -> None:
        self.pidSource = ...
        self.valueEntry = ...
    
    def calibrate(self) -> None:
        ...
    
    def reset(self) -> None:
        ...
    
    def getAngle(self) -> float:
        ...
    
    def getRate(self) -> float:
        ...
    
    def setPIDSourceType(self, pidSource: PIDSourceType) -> None:
        """Set which parameter of the gyro you are using as a process
        control variable. The Gyro class supports the rate and angle
        parameters.

        :param pidSource: An enum to select the parameter.
        """
        self.pidSource = ...
    
    def getPIDSourceType(self) -> PIDSourceType:
        ...
    
    def pidGet(self) -> float:
        """Get the output of the gyro for use with PIDControllers. May be
        the angle or rate depending on the set :class:`.PIDSourceType`

        :returns: the current angle according to the gyro
        """
        ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    


