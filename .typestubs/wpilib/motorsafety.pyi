"""
This type stub file was generated by pyright.
"""

import logging

"""
This type stub file was generated by pyright.
"""
logger = logging.getLogger(__name__)
__all__ = ["MotorSafety"]
class MotorSafety:
    """Provides mechanisms to safely shutdown motors if they aren't updated
    often enough.

    This base class runs a watchdog timer and calls the subclass's stopMotor()
    function if the timeout expires.

    The subclass should call feed() whenever the motor value is updated.
    """
    DEFAULT_SAFETY_EXPIRATION = ...
    __instanceList = ...
    __listMutex = ...
    @classmethod
    def _reset(cls) -> None:
        ...
    
    def __init__(self) -> None:
        ...
    
    def feed(self) -> None:
        """Feed the motor safety object.

        Resets the timer on this object that is used to do the timeouts.
        """
        ...
    
    def setExpiration(self, expirationTime: float) -> None:
        """Set the expiration time for the corresponding motor safety object.

        :param expirationTime: The timeout value in seconds.
        """
        ...
    
    def getExpiration(self) -> float:
        """Retrieve the timeout value for the corresponding motor safety object.

        :returns: the timeout value in seconds.
        """
        ...
    
    def isAlive(self) -> bool:
        """Determine of the motor is still operating or has timed out.

        :returns: True if the motor is still operating normally and hasn't
            timed out.
        """
        ...
    
    def check(self) -> None:
        """Check if this motor has exceeded its timeout.
        This method is called periodically to determine if this motor has
        exceeded its timeout value. If it has, the stop method is called,
        and the motor is shut down until its value is updated again.
        """
        ...
    
    def setSafetyEnabled(self, enabled: bool) -> None:
        """Enable/disable motor safety for this device.

        Turn on and off the motor safety option for this PWM object.

        :param enabled: True if motor safety is enforced for this object
        """
        ...
    
    def isSafetyEnabled(self) -> bool:
        """Return the state of the motor safety enabled flag.

        Return if the motor safety is currently enabled for this device.

        :returns: True if motor safety is enforced for this device
        """
        ...
    
    @classmethod
    def checkMotors(cls) -> None:
        """Check the motors to see if any have timed out.
        This static method is called periodically to poll all the motors and
        stop any that have timed out.
        """
        ...
    
    def stopMotor(self) -> None:
        ...
    
    def getDescription(self) -> str:
        ...
    

