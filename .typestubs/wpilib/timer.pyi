"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ["Timer"]
class Timer:
    """
        Provides time-related functionality for the robot
        
        .. note:: Prefer to use this module for time functions, instead of
                  the :mod:`time` module in the standard library. This will
                  make it easier for your code to work properly in simulation. 
    """
    @staticmethod
    def getFPGATimestamp() -> float:
        """Return the system clock time in seconds. Return the time from the
        FPGA hardware clock in seconds since the FPGA started.

        :returns: Robot running time in seconds.
        """
        ...
    
    @staticmethod
    def getMatchTime() -> float:
        """Return the approximate match time.
        The FMS does not currently send the official match time to the robots,
        but does send an approximate match time. The value will count down
        the time remaining in the current period (auto or teleop). 
        
        .. warning::
            This is not an official time (so it cannot be used to dispute ref
            calls or guarantee that a function will trigger before the match ends).

        The Practice Match function of the DS approximates the behavior seen
        on the field.

        :returns: Time remaining in current match period (auto or teleop) in seconds
        """
        ...
    
    @staticmethod
    def delay(seconds: float) -> None:
        """Pause the thread for a specified time. Pause the execution of the
        thread for a specified period of time given in seconds. Motors will
        continue to run at their last assigned values, and sensors will
        continue to update. Only the thread containing the wait will pause
        until the wait time is expired.

        :param seconds: Length of time to pause

        .. warning:: If you're tempted to use this function for autonomous
                     mode to time transitions between actions, don't do it!
                     
                     Delaying the main robot thread for more than a few
                     milliseconds is generally discouraged, and will cause
                     problems and possibly leave the robot unresponsive.
                     
        """
        ...
    
    def __init__(self) -> None:
        self.mutex = ...
        self.startTime = ...
        self.accumulatedTime = ...
        self.running = ...
    
    def getMsClock(self) -> int:
        """
            :returns: the system clock time in milliseconds.
        """
        ...
    
    def get(self) -> float:
        """Get the current time from the timer. If the clock is running it is
        derived from the current system clock the start time stored in the
        timer class. If the clock is not running, then return the time when
        it was last stopped.

        :returns: Current time value for this timer in seconds
        """
        ...
    
    def reset(self) -> None:
        """Reset the timer by setting the time to 0.
        Make the timer startTime the current time so new requests will be
        relative now.
        """
        ...
    
    def start(self) -> None:
        """Start the timer running.
        Just set the running flag to true indicating that all time requests
        should be relative to the system clock.
        """
        ...
    
    def stop(self) -> None:
        """Stop the timer.
        This computes the time as of now and clears the running flag, causing
        all subsequent time requests to be read from the accumulated time
        rather than looking at the system clock.
        """
        ...
    
    def hasPeriodPassed(self, period: float) -> bool:
        """Check if the period specified has passed and if it has, advance the start
        time by that period. This is useful to decide if it's time to do periodic
        work without drifting later by the time it took to get around to checking.
 
        :param period: The period to check for (in seconds).
        :returns: If the period has passed.
        """
        ...
    


