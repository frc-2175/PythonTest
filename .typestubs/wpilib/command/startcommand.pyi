"""
This type stub file was generated by pyright.
"""

from .command import Command
from .instantcommand import InstantCommand

"""
This type stub file was generated by pyright.
"""
__all__ = ["StartCommand"]
class StartCommand(InstantCommand):
    """A StartCommand will call the start() method of another command when it
    is initialized and will finish immediately.
    """
    def __init__(self, commandToStart: Command) -> None:
        """Instantiates a StartCommand which will start the
        given command whenever its initialize() is called.

        :param commandToStart: the :class:`.Command` to start
        """
        self.commandToFork = ...
    
    def initialize(self) -> None:
        ...
    

