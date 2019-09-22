"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ["Utility"]
class Utility:
    """Contains global utility functions

    .. deprecated:: 2018.0.0
        Use :class:`.RobotController` instead
    """
    @staticmethod
    def getFPGAVersion() -> int:
        """Return the FPGA Version number.

        .. deprecated:: 2018.0.0
            Use :meth:`.RobotController.getFPGAVersion` instead

        :returns: FPGA Version number.
        """
        ...
    
    @staticmethod
    def getFPGARevision() -> int:
        """Return the FPGA Revision number. The format of the revision is 3
        numbers.  The 12 most significant bits are the Major Revision. the
        next 8 bits are the Minor Revision. The 12 least significant bits
        are the Build Number.

        .. deprecated:: 2018.0.0
            Use :meth:`.RobotController.getFPGARevision` instead

        :returns: FPGA Revision number.
        """
        ...
    
    @staticmethod
    def getFPGATime() -> int:
        """Read the microsecond timer from the FPGA.

        .. deprecated:: 2018.0.0
            Use :meth:`.RobotController.getFPGATime` instead

        :returns: The current time in microseconds according to the FPGA.
        """
        ...
    
    @staticmethod
    def getUserButton() -> bool:
        """Get the state of the "USER" button on the roboRIO.

        .. deprecated:: 2018.0.0
            Use :meth:`.RobotController.getUserButton` instead

        :returns: True if the button is currently pressed down
        """
        ...
    


