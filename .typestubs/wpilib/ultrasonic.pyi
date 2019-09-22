"""
This type stub file was generated by pyright.
"""

import enum
from typing import Union
from .digitalinput import DigitalInput
from .digitaloutput import DigitalOutput
from .sendablebase import SendableBase
from .sendablebuilder import SendableBuilder

"""
This type stub file was generated by pyright.
"""
__all__ = ["Ultrasonic"]
class Ultrasonic(SendableBase):
    """Ultrasonic rangefinder control
    
    The Ultrasonic rangefinder measures
    absolute distance based on the round-trip time of a ping generated by
    the controller.  These sensors use two transducers, a speaker and a
    microphone both tuned to the ultrasonic range. A common ultrasonic
    sensor, the Daventech SRF04 requires a short pulse to be generated on
    a digital channel. This causes the chirp to be emitted. A second line
    becomes high as the ping is transmitted and goes low when the echo is
    received. The time that the line is high determines the round trip
    distance (time of flight).
    
    .. not_implemented: initialize
    """
    class Unit(enum.IntEnum):
        """The units to return when PIDGet is called"""
        kInches = ...
        kMillimeters = ...
    
    
    kPingTime = ...
    kPriority = ...
    kMaxUltrasonicTime = ...
    kSpeedOfSoundInchesPerSec = ...
    PIDSourceType = ...
    _static_mutex = ...
    sensors = ...
    automaticEnabled = ...
    instances = ...
    _thread = ...
    @staticmethod
    def isAutomaticMode() -> bool:
        ...
    
    @staticmethod
    def ultrasonicChecker() -> None:
        """Background task that goes through the list of ultrasonic sensors
        and pings each one in turn. The counter is configured to read the
        timing of the returned echo pulse.

        .. warning:: DANGER WILL ROBINSON, DANGER WILL ROBINSON: This code runs
            as a task and assumes that none of the ultrasonic sensors will
            change while it's running. If one does, then this will certainly
            break. Make sure to disable automatic mode before changing
            anything with the sensors!!
        """
        ...
    
    def __init__(self, pingChannel: Union[DigitalOutput, int], echoChannel: Union[DigitalInput, int], units: Unit = ...) -> None:
        """Create an instance of the Ultrasonic Sensor.
        This is designed to supchannel the Daventech SRF04 and Vex ultrasonic
        sensors.

        :param pingChannel: The digital output channel that sends the pulse
            to initiate the sensor sending the ping.
        :param echoChannel: The digital input channel that receives the echo.
            The length of time that the echo is high represents the round
            trip time of the ping, and the distance.
        :param units: The units returned in either kInches or kMillimeters
        """
        self.pingAllocated = ...
        self.echoAllocated = ...
        self.pingChannel = ...
        self.echoChannel = ...
        self.units = ...
        self.pidSource = ...
        self.enabled = ...
        self.valueEntry = ...
        self.counter = ...
    
    def close(self) -> None:
        ...
    
    def setAutomaticMode(self, enabling: bool) -> None:
        """Turn Automatic mode on/off. When in Automatic mode, all sensors
        will fire in round robin, waiting a set time between each sensor.

        :param enabling:
            Set to true if round robin scheduling should start for all the
            ultrasonic sensors. This scheduling method assures that the
            sensors are non-interfering because no two sensors fire at the
            same time. If another scheduling algorithm is preferred, it
            can be implemented by pinging the sensors manually and waiting
            for the results to come back.
        """
        ...
    
    def ping(self) -> None:
        """Single ping to ultrasonic sensor. Send out a single ping to the
        ultrasonic sensor. This only works if automatic (round robin) mode is
        disabled. A single ping is sent out, and the counter should count the
        semi-period when it comes in. The counter is reset to make the current
        value invalid.
        """
        ...
    
    def isRangeValid(self) -> bool:
        """Check if there is a valid range measurement. The ranges are
        accumulated in a counter that will increment on each edge of the
        echo (return) signal. If the count is not at least 2, then the range
        has not yet been measured, and is invalid.

        :returns: True if the range is valid
        """
        ...
    
    def getRangeInches(self) -> float:
        """Get the range in inches from the ultrasonic sensor.

        :returns: Range in inches of the target returned from the ultrasonic
            sensor. If there is no valid value yet, i.e. at least one
            measurement hasn't completed, then return 0.
        """
        ...
    
    def getRangeMM(self) -> float:
        """Get the range in millimeters from the ultrasonic sensor.

        :returns: Range in millimeters of the target returned by the
            ultrasonic sensor. If there is no valid value yet, i.e. at least
            one measurement hasn't complted, then return 0.
        """
        ...
    
    def setPIDSourceType(self, pidSource: PIDSourceType) -> None:
        """Set which parameter you are using as a process
        control variable. 

        :param pidSource: An enum to select the parameter.
        """
        self.pidSource = ...
    
    def getPIDSourceType(self) -> PIDSourceType:
        ...
    
    def pidGet(self) -> float:
        """Get the range in the current DistanceUnit (PIDSource interface).

        :returns: The range in DistanceUnit
        """
        ...
    
    def setDistanceUnits(self, units: Unit) -> None:
        """Set the current DistanceUnit that should be used for the
        PIDSource interface.

        :param units: The DistanceUnit that should be used.
        """
        self.units = ...
    
    def getDistanceUnits(self) -> Unit:
        """Get the current DistanceUnit that is used for the PIDSource
        interface.

        :returns: The type of DistanceUnit that is being used.
        """
        ...
    
    def isEnabled(self) -> bool:
        """Is the ultrasonic enabled.

        :returns: True if the ultrasonic is enabled
        """
        ...
    
    def setEnabled(self, enable: bool) -> None:
        """Set if the ultrasonic is enabled.

        :param enable: set to True to enable the ultrasonic
        """
        self.enabled = ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    


