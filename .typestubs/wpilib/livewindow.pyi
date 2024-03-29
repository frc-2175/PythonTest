"""
This type stub file was generated by pyright.
"""

import logging
from typing import Optional, Union
from networktables.entry import NetworkTableEntry
from networktables.networktable import NetworkTable
from .sendable import Sendable

"""
This type stub file was generated by pyright.
"""
logger = logging.getLogger(__name__)
__all__ = ["LiveWindow"]
class Component:
    def __init__(self, sendable: Sendable, parent: Optional[Sendable]) -> None:
        self.sendable = ...
        self.parent = ...
        self.builder = ...
        self.firstTime = ...
        self.telemetryEnabled = ...
    


class _LiveWindowComponent:
    """A LiveWindow component is a device (sensor or actuator) that should be
    added to the SmartDashboard in test mode. The components are cached until
    the first time the robot enters Test mode. This allows the components to
    be inserted, then renamed."""
    def __init__(self, subsystem, name: str, isSensor: bool) -> None:
        self.subsystem = ...
        self.name = ...
        self.isSensor = ...
    


class LiveWindow:
    """The public interface for putting sensors and
    actuators on the LiveWindow."""
    components = ...
    _liveWindowTable = ...
    _statusTable = ...
    _enabledEntry = ...
    startLiveWindow = ...
    liveWindowEnabled = ...
    telemetryEnabled = ...
    mutex = ...
    @classmethod
    def liveWindowTable(cls) -> NetworkTable:
        ...
    
    @classmethod
    def statusTable(cls) -> NetworkTable:
        ...
    
    @classmethod
    def enabledEntry(cls) -> NetworkTableEntry:
        ...
    
    @classmethod
    def _reset(cls) -> None:
        ...
    
    @classmethod
    def isEnabled(cls) -> bool:
        ...
    
    @classmethod
    def setEnabled(cls, enabled: bool) -> None:
        """Set the enabled state of LiveWindow. If it's being enabled, turn
        off the scheduler and remove all the commands from the queue and
        enable all the components registered for LiveWindow. If it's being
        disabled, stop all the registered components and reenable the
        scheduler.

        TODO: add code to disable PID loops when enabling LiveWindow. The
        commands should reenable the PID loops themselves when they get
        rescheduled. This prevents arms from starting to move around, etc.
        after a period of adjusting them in LiveWindow mode.
        """
        ...
    
    @classmethod
    def run(cls) -> None:
        """The run method is called repeatedly to keep the values refreshed
        on the screen in test mode.

        .. deprecated:: 2018.0.0
            No longer required
        """
        ...
    
    @classmethod
    def addSensor(cls, subsystem: str, name: Union[str, int], component: Sendable) -> None:
        """Add a Sensor associated with the subsystem and with call it by the
        given name.

        :param subsystem: The subsystem this component is part of.
        :param name: The name of this component.
        :param component: A LiveWindowSendable component that represents a
            sensor.

        .. deprecated:: 2018.0.0
            Use :meth:`.Sendable.setName` instead.
        """
        ...
    
    @classmethod
    def addActuator(cls, subsystem: str, name: str, component: Sendable) -> None:
        """Add an Actuator associated with the subsystem and with call it by
        the given name.

        :param subsystem: The subsystem this component is part of.
        :param name: The name of this component.
        :param component: A LiveWindowSendable component that represents a actuator.

        .. deprecated:: 2018.0.0
            Use :meth:`.Sendable.setName` instead.
        """
        ...
    
    @classmethod
    def addSensorChannel(cls, moduleType: str, channel: int, component: Sendable) -> None:
        """Add Sensor to LiveWindow. The components are shown with the type
        and channel like this: Gyro[0] for a gyro object connected to the
        first analog channel.

        :param moduleType: A string indicating the type of the module used in
            the naming (above)
        :param channel: The channel number the device is connected to
        :param component: A reference to the object being added

        .. deprecated:: 2018.0.0
            Use :meth:`.SendableBase.setName` instead.
        """
        ...
    
    @classmethod
    def addActuatorChannel(cls, moduleType: str, channel: int, component: Sendable) -> None:
        """Add Actuator to LiveWindow. The components are shown with the
        module type, slot and channel like this: Servo[0,2] for a servo
        object connected to the first digital module and PWM port 2.

        :param moduleType: A string that defines the module name in the label
            for the value
        :param channel: The channel number the device is plugged into
            (usually PWM)
        :param component: The reference to the object being added

        .. deprecated:: 2018.0.0
            Use :meth:`.SendableBase.setName` instead.
        """
        ...
    
    @classmethod
    def addActuatorModuleChannel(cls, moduleType: str, moduleNumber: int, channel: int, component: Sendable) -> None:
        """Add Actuator to LiveWindow. The components are shown with the
        module type, slot and channel like this: Servo[0,2] for a servo
        object connected to the first digital module and PWM port 2.

        :param moduleType: A string that defines the module name in the label
            for the value
        :param moduleNumber: The number of the particular module type
        :param channel: The channel number the device is plugged into
            (usually PWM)
        :param component: The reference to the object being added

        .. deprecated:: 2018.0.0
            Use :meth:`.SendableBase.setName` instead.
        """
        ...
    
    @classmethod
    def add(cls, sendable: Sendable) -> None:
        """
        Add a component to the LiveWindow.

        :param sendable: component to add
        """
        ...
    
    @classmethod
    def addChild(cls, parent: Sendable, child: object) -> None:
        """
        Add a child component to a component.

        :param parent: parent component
        :param child: child component
        """
        ...
    
    @classmethod
    def remove(cls, sendable: Sendable) -> None:
        """
        Remove a component from the LiveWindow.

        :param sendable: component to remove
        """
        ...
    
    @classmethod
    def enableTelemetry(cls, sendable: Sendable) -> None:
        """
        Enable telemetry for a single component.

        :param sendable: component
        """
        ...
    
    @classmethod
    def disableTelemetry(cls, sendable: Sendable) -> None:
        """
        Disable telemetry for a single component.  

        :param sendable: component
        """
        ...
    
    @classmethod
    def disableAllTelemetry(cls) -> None:
        """ Disable ALL telemetry """
        ...
    
    @classmethod
    def updateValues(cls) -> None:
        ...
    


