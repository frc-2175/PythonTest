"""
This type stub file was generated by pyright.
"""

from .instantcommand import InstantCommand

"""
This type stub file was generated by pyright.
"""
__all__ = ["PrintCommand"]
class PrintCommand(InstantCommand):
    """A PrintCommand is a command which prints out a string when it is
    initialized, and then immediately finishes.

    It is useful if you want a :class:`.CommandGroup` to print out a string when it
    reaches a certain point.
    """
    def __init__(self, message: str) -> None:
        """Instantiates a PrintCommand which will print the given message when
        it is run.
        
        :param message: the message to print
        """
        self.message = ...
    
    def initialize(self) -> None:
        ...
    


