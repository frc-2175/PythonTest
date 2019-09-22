"""
This type stub file was generated by pyright.
"""

from ..command import command
from ..sendablebase import SendableBase
from ..sendablebuilder import SendableBuilder

"""
This type stub file was generated by pyright.
"""
__all__ = ["Trigger"]
class Trigger(SendableBase):
    """This class provides an easy way to link commands to inputs.

    It is very easy to link a button to a command.  For instance, you could
    link the trigger button of a joystick to a "score" command.

    It is encouraged that teams write a subclass of Trigger if they want to
    have something unusual (for instance, if they want to react to the user
    holding a button while the robot is reading a certain sensor input).
    For this, they only have to write the :func:`get` method to get the full
    functionality of the Trigger class.
    """
    def get(self) -> bool:
        """Returns whether or not the trigger is active

        This method will be called repeatedly a command is linked to the
        Trigger.

        :returns: whether or not the trigger condition is active.
        """
        ...
    
    def grab(self) -> bool:
        """Returns whether :meth:`get` returns True or the internal table for
        :class:`.SmartDashboard` use is pressed.
        """
        ...
    
    def whenActive(self, command: command.Command) -> None:
        """Starts the given command whenever the trigger just becomes active.

        :param command: the command to start
        """
        ...
    
    def whileActive(self, command: command.Command) -> None:
        """Constantly starts the given command while the button is held.

        :meth:`Command.start` will be called repeatedly while the trigger is
        active, and will be canceled when the trigger becomes inactive.

        :param command: the command to start
        """
        ...
    
    def whenInactive(self, command: command.Command) -> None:
        """Starts the command when the trigger becomes inactive.

        :param command: the command to start
        """
        ...
    
    def toggleWhenActive(self, command: command.Command) -> None:
        """Toggles a command when the trigger becomes active.

        :param command: the command to toggle
        """
        ...
    
    def cancelWhenActive(self, command: command.Command) -> None:
        """Cancels a command when the trigger becomes active.

        :param command: the command to cancel
        """
        ...
    
    def _safeState(self) -> None:
        self.sendablePressed = ...
    
    def _setPressed(self, value: bool) -> None:
        self.sendablePressed = ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    


