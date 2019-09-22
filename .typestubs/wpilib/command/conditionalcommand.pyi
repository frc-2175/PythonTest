"""
This type stub file was generated by pyright.
"""

from .command import Command
from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
__all__ = ["ConditionalCommand"]
class ConditionalCommand(Command):
    """
        A ConditionalCommand is a :class:`.Command` that starts one of two commands.
        
        A ConditionalCommand uses m_condition to determine whether it should run m_onTrue or
        m_onFalse.
        
        A ConditionalCommand adds the proper :class:`.Command` to the :class:`.Scheduler` during
        :meth:`initialize` and then :meth:`isFinished` will
        return true once that :class:`.Command` has finished executing.
        
        If no :class:`.Command` is specified for m_onFalse, the occurrence of that condition will be a
        no-op.
        
        @see :class:`.Command`
        @see :class:`.Scheduler`
    """
    def __init__(self, name, onTrue: Optional[Any] = ..., onFalse: Optional[Any] = ...):
        """Creates a new ConditionalCommand with given name and onTrue and onFalse Commands.
        
        Users of this constructor should also override condition().
        
        :param name: the name for this command group
        :param onTrue: The Command to execute if {@link ConditionalCommand#condition()} returns true
        :param onFalse: The Command to execute if {@link ConditionalCommand#condition()} returns false
        """
        self.onTrue = ...
        self.onFalse = ...
        self.chosenCommand = ...
    
    def requireAll(self):
        ...
    
    def condition(self):
        """The Condition to test to determine which Command to run.
        
        :returns: true if m_onTrue should be run or false if m_onFalse should be run.
        """
        ...
    
    def _initialize(self):
        """
            Calls condition() and runs the proper command.
        """
        ...
    
    def _cancel(self):
        ...
    
    def isFinished(self):
        ...
    
    def _interrupted(self):
        ...
    


