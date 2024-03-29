"""
This type stub file was generated by pyright.
"""

import hal
from .sendablebuilder import SendableBuilder
from .solenoidbase import SolenoidBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["Solenoid"]
def _freeSolenoid(solenoidHandle: hal.SolenoidHandle) -> None:
    ...

class Solenoid(SolenoidBase):
    """Solenoid class for running high voltage Digital Output.

    The Solenoid class is typically used for pneumatic solenoids, but could
    be used for any device within the current spec of the PCM.
    
    .. not_implemented: initSolenoid
    """
    def __init__(self, *args, **kwargs) -> None:
        """Constructor.

        Arguments can be supplied as positional or keyword.  Acceptable
        positional argument combinations are:
        
        - channel
        - moduleNumber, channel

        Alternatively, the above names can be used as keyword arguments.

        :param moduleNumber: The CAN ID of the PCM the solenoid is attached to
        :type moduleNumber: int
        :param channel: The channel on the PCM to control (0..7)
        :type channel: int
        """
        self.channel = ...
        self.solenoidHandle = ...
    
    def close(self) -> None:
        """Mark the solenoid as close."""
        self.solenoidHandle = ...
    
    def set(self, on: bool) -> None:
        """Set the value of a solenoid.

        :param on: True will turn the solenoid output on. False will turn the solenoid output off.
        """
        ...
    
    def get(self) -> bool:
        """Read the current value of the solenoid.

        :returns: True if the solenoid output is on or false if the solenoid output is off.
        """
        ...
    
    def isBlackListed(self) -> bool:
        """
        Check if the solenoid is blacklisted.
            If a solenoid is shorted, it is added to the blacklist and disabled until power cycle, or until faults are
            cleared. See :meth:`.SolenoidBase.clearAllPCMStickyFaults`

        :returns: If solenoid is disabled due to short.
        """
        ...
    
    def setPulseDuration(self, durationSeconds: float) -> None:
        """
        Set the pulse duration in the PCM. This is used in conjunction with
        the startPulse method to allow the PCM to control the timing of a pulse.
        The timing can be controlled in 0.01 second increments.

        see :meth:`startPulse`

        :param durationSeconds: The duration of the pulse, from 0.01 to 2.55 seconds.
        """
        ...
    
    def startPulse(self) -> None:
        """
        Trigger the PCM to generate a pulse of the duration set in
        setPulseDuration.

        see :meth:`setPulseDuration`
        """
        ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    


