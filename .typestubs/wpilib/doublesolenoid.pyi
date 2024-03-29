"""
This type stub file was generated by pyright.
"""

import hal
import enum
from .sendablebuilder import SendableBuilder
from .solenoidbase import SolenoidBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["DoubleSolenoid"]
def _freeSolenoid(fwdHandle: hal.SolenoidHandle, revHandle: hal.SolenoidHandle) -> None:
    ...

class DoubleSolenoid(SolenoidBase):
    """Controls 2 channels of high voltage Digital Output on the PCM.

    The DoubleSolenoid class is typically used for pneumatics solenoids that
    have two positions controlled by two separate channels.
    """
    class Value(enum.IntEnum):
        """Possible values for a DoubleSolenoid."""
        kOff = ...
        kForward = ...
        kReverse = ...
    
    
    def __init__(self, *args, **kwargs) -> None:
        """Constructor.

        Arguments can be supplied as positional or keyword.  Acceptable
        positional argument combinations are:
        
        - forwardChannel, reverseChannel
        - moduleNumber, forwardChannel, reverseChannel

        Alternatively, the above names can be used as keyword arguments.

        :param moduleNumber: The module number of the solenoid module to use.
        :param forwardChannel: The forward channel number on the module to control (0..7)
        :param reverseChannel: The reverse channel number on the module to control  (0..7)
        """
        self.valueEntry = ...
        self.forwardHandle = ...
        self.forwardMask = ...
        self.reverseMask = ...
    
    def close(self) -> None:
        """Mark the solenoid as freed."""
        self.forwardHandle = ...
        self.reverseHandle = ...
    
    def set(self, value: Value) -> None:
        """Set the value of a solenoid.

        :param value: The value to set (Off, Forward, Reverse)
        """
        ...
    
    def get(self) -> Value:
        """Read the current value of the solenoid.

        :returns: The current value of the solenoid.
        """
        ...
    
    def isFwdSolenoidBlackListed(self) -> bool:
        """
        Check if the forward solenoid is blacklisted.
            If a solenoid is shorted, it is added to the blacklist and disabled until power cycle, or until faults are
            cleared. See :meth:`clearAllPCMStickyFaults`

        :returns: If solenoid is disabled due to short.
        """
        ...
    
    def isRevSolenoidBlackListed(self) -> bool:
        """
        Check if the reverse solenoid is blacklisted.
            If a solenoid is shorted, it is added to the blacklist and disabled until power cycle, or until faults are
            cleared. See :meth:`clearAllPCMStickyFaults`

        :returns: If solenoid is disabled due to short.
        """
        ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    
    def _valueChanged(self, value: str) -> None:
        ...
    


