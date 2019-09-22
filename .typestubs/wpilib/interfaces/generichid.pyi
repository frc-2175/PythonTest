"""
This type stub file was generated by pyright.
"""

import enum

"""
This type stub file was generated by pyright.
"""
__all__ = ["GenericHID"]
class GenericHID:
    """
    GenericHID Interface.
    """
    class RumbleType(enum.IntEnum):
        """Represents a rumble output on the JoyStick."""
        kLeftRumble = ...
        kRightRumble = ...
    
    
    class HIDType(enum.IntEnum):
        kUnknown = ...
        kXInputUnknown = ...
        kXInputGamepad = ...
        kXInputWheel = ...
        kXInputArcadeStick = ...
        kXInputFlightStick = ...
        kXInputDancePad = ...
        kXInputGuitar = ...
        kXInputGuitar2 = ...
        kXInputDrumKit = ...
        kXInputGuitar3 = ...
        kXInputArcadePad = ...
        kHIDJoystick = ...
        kHIDGamepad = ...
        kHIDDriving = ...
        kHIDFlight = ...
        kHID1stPerson = ...
    
    
    class Hand(enum.IntEnum):
        """Which hand the Human Interface Device is associated with."""
        kLeft = ...
        kRight = ...
    
    
    def __init__(self, port: int) -> None:
        self.port = ...
        self.ds = ...
        self.outputs = ...
        self.leftRumble = ...
        self.rightRumble = ...
    
    def getX(self, hand: Hand = ...) -> float:
        """Get the x position of HID.

        :param hand: which hand, left or right
        :returns: the x position
        """
        ...
    
    def getY(self, hand: Hand = ...) -> float:
        """Get the y position of the HID.

        :param hand: which hand, left or right
        :returns: the y position
        """
        ...
    
    def getRawButton(self, button: int) -> bool:
        """Get the button value (starting at button 1).

        :param button: The button number to be read (starting at 1)
        :returns: The state of the button.
        """
        ...
    
    def getRawButtonPressed(self, button: int) -> bool:
        """Whether the button was pressed since the last check. Button indexes begin at 1.

        :param button: The button index, beginning at 1.
        :returns: Whether the button was pressed since the last check.

        .. versionadded:: 2018.0.0
        """
        ...
    
    def getRawButtonReleased(self, button: int) -> bool:
        """Whether the button was released since the last check. Button indexes begin at 1.

        :param button: The button index, beginning at 1.
        :returns: Whether the button was released since the last check.

        .. versionadded:: 2018.0.0
        """
        ...
    
    def getRawAxis(self, axis: int) -> float:
        """Get the raw axis.

        :param axis: index of the axis
        :returns: the raw value of the selected axis
        """
        ...
    
    def getPOV(self, pov: int = ...) -> int:
        """Get the angle in degrees of a POV on the HID.

        The POV angles start at 0 in the up direction, and increase clockwise (eg right is 90,
        upper-left is 315).

        :param pov: The index of the POV to read (starting at 0)
        :returns: the angle of the POV in degrees, or -1 if the POV is not pressed.
        """
        ...
    
    def getAxisCount(self) -> int:
        """Get the number of axes for the HID

        :returns: The number of axis for the current HID
        """
        ...
    
    def getPOVCount(self) -> int:
        """For the current HID, return the number of POVs."""
        ...
    
    def getButtonCount(self) -> int:
        """For the current HID, return the number of buttons."""
        ...
    
    def getPort(self) -> int:
        """Get the port number of the HID.

        :returns: The port number of the HID.
        """
        ...
    
    def getType(self) -> HIDType:
        """Get the type of the HID.

        :returns: the type of the HID.
        """
        ...
    
    def getName(self) -> str:
        """Get the name of the HID.

        :returns: the name of the HID.
        """
        ...
    
    def setOutput(self, outputNumber: int, value: bool) -> None:
        """Set a single HID output value for the HID.

        :param outputNumber: The index of the output to set (1-32)
        :param value: The value to set the output to
        """
        self.outputs = ...
    
    def setOutputs(self, value: int) -> None:
        """Set all HID output values for the HID.

        :param value: The 32 bit output value (1 bit for each output)
        """
        self.outputs = ...
    
    def setRumble(self, type: RumbleType, value: float) -> None:
        """Set the rumble output for the HID. The DS currently supports 2 rumble values, left rumble and
        right rumble.

        :param type: Which rumble value to set
        :param value: The normalized value (0 to 1) to set the rumble to
        """
        ...
    


