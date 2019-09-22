"""
This type stub file was generated by pyright.
"""

from ..sendablebase import SendableBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["Scheduler"]
class Scheduler(SendableBase):
    """The Scheduler is a singleton which holds the top-level running commands.
    It is in charge of both calling the command's run() method and to make
    sure that there are no two commands with conflicting requirements running.

    It is fine if teams wish to take control of the Scheduler themselves, all
    that needs to be done is to call Scheduler.getInstance().run() often to
    have Commands function correctly. However, this is already done for you
    if you use the CommandBased Robot template.

    .. seealso:: :class:`.Command`
    """
    @staticmethod
    def _reset():
        ...
    
    @staticmethod
    def getInstance():
        """Returns the Scheduler, creating it if one does not exist.

        :returns: the Scheduler
        """
        ...
    
    def __init__(self):
        """Instantiates a Scheduler.
        """
        self.commandTable = ...
        self.subsystems = ...
        self.adding = ...
        self.disabled = ...
        self.additions = ...
        self.buttons = ...
        self.runningCommandsChanged = ...
        self.namesEntry = ...
        self.idsEntry = ...
        self.cancelEntry = ...
    
    def add(self, command):
        """Adds the command to the Scheduler. This will not add the
        :class:`.Command` immediately, but will instead wait for the proper time in
        the :meth:`run` loop before doing so. The command returns immediately
        and does nothing if given null.

        Adding a :class:`.Command` to the :class:`.Scheduler` involves the
        Scheduler removing any Command which has shared requirements.

        :param command: the command to add
        """
        ...
    
    def addButton(self, button):
        """Adds a button to the Scheduler. The Scheduler will poll
        the button during its :meth:`run`.

        :param button: the button to add
        """
        ...
    
    def _add(self, command):
        """Adds a command immediately to the Scheduler. This should only be
        called in the :meth:`run` loop. Any command with conflicting
        requirements will be removed, unless it is uninterruptable. Giving
        None does nothing.

        :param command: the :class:`.Command` to add
        """
        ...
    
    def run(self):
        """Runs a single iteration of the loop. This method should be called
        often in order to have a functioning Command system. The loop has five
        stages:

        - Poll the Buttons
        - Execute/Remove the Commands
        - Send values to SmartDashboard
        - Add Commands
        - Add Defaults
        """
        self.runningCommandsChanged = ...
    
    def registerSubsystem(self, system):
        """Registers a :class:`.Subsystem` to this Scheduler, so that the
        Scheduler might know if a default Command needs to be
        run. All :class:`.Subsystem` objects should call this.

        :param system: the system
        """
        ...
    
    def remove(self, command):
        """Removes the :class:`.Command` from the Scheduler.

        :param command: the command to remove
        """
        ...
    
    def removeAll(self):
        """Removes all commands
        """
        ...
    
    def disable(self):
        """Disable the command scheduler.
        """
        self.disabled = ...
    
    def enable(self):
        """Enable the command scheduler.
        """
        self.disabled = ...
    
    def initSendable(self, builder):
        self.namesEntry = ...
        self.idsEntry = ...
        self.cancelEntry = ...
    
    def _updateTable(self):
        ...
    


