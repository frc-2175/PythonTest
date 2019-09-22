"""
This type stub file was generated by pyright.
"""

from .command import Command

"""
This type stub file was generated by pyright.
"""
__all__ = ["WaitUntilCommand"]
class WaitUntilCommand(Command):
    """
    This will wait until the game clock reaches some value, then continue to
    the next command.
    """
    def __init__(self, time: float) -> None:
        self.time = ...
    
    def isFinished(self) -> bool:
        ...
    


