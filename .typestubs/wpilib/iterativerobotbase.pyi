"""
This type stub file was generated by pyright.
"""

import enum
from .robotbase import RobotBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["IterativeRobotBase"]
class IterativeRobotBase(RobotBase):
    """IterativeRobotBase implements a specific type of robot program framework, extending the RobotBase
    class.

    The IterativeRobotBase class does not implement startCompetition(), so it should not be used
    by teams directly.

    This class provides the following functions which are called by the main loop,
    startCompetition(), at the appropriate times:

    robotInit() -- provide for initialization at robot power-on

    init() functions -- each of the following functions is called once when the
    appropriate mode is entered:

    - disabledInit()   -- called each and every time disabled is entered from
      another mode
    - autonomousInit() -- called each and every time autonomous is entered from
      another mode
    - teleopInit()     -- called each and every time teleop is entered from
      another mode
    - testInit()       -- called each and every time test is entered from
      another mode

    periodic() functions -- each of these functions is called on an interval:

    - robotPeriodic()
    - disabledPeriodic()
    - autonomousPeriodic()
    - teleopPeriodic()
    - testPeriodic()
    """
    class Mode(enum.IntEnum):
        kNone = ...
        kDisabled = ...
        kAutonomous = ...
        kTeleop = ...
        kTest = ...
    
    
    logger = ...
    def __init__(self, period: float) -> None:
        """Constructor for IterativeRobotBase.

        :param period: Period in seconds
        """
        self.last_mode = ...
        self.period = ...
        self.watchdog = ...
    
    def robotInit(self) -> None:
        """Robot-wide initialization code should go here.

        Users should override this method for default Robot-wide initialization
        which will be called when the robot is first powered on.  It will be
        called exactly 1 time.

        .. note:: It is simpler to override this function instead of defining
                  a constructor for your robot class
        """
        ...
    
    def disabledInit(self) -> None:
        """Initialization code for disabled mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters disabled mode.
        """
        ...
    
    def autonomousInit(self) -> None:
        """Initialization code for autonomous mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters autonomous mode.
        """
        ...
    
    def teleopInit(self) -> None:
        """Initialization code for teleop mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters teleop mode.
        """
        ...
    
    def testInit(self) -> None:
        """Initialization code for test mode should go here.

        Users should override this method for initialization code which will be
        called each time the robot enters test mode.
        """
        ...
    
    def robotPeriodic(self) -> None:
        """Periodic code for all robot modes should go here."""
        ...
    
    def disabledPeriodic(self) -> None:
        """Periodic code for disabled mode should go here."""
        ...
    
    def autonomousPeriodic(self) -> None:
        """Periodic code for autonomous mode should go here."""
        ...
    
    def teleopPeriodic(self) -> None:
        """Periodic code for teleop mode should go here."""
        ...
    
    def testPeriodic(self) -> None:
        """Periodic code for test mode should go here."""
        ...
    
    def loopFunc(self) -> None:
        """Call the appropriate function depending upon the current robot mode"""
        ...
    
    def printLoopOverrunMessage(self) -> None:
        ...
    


