"""
This type stub file was generated by pyright.
"""

from .pwmspeedcontroller import PWMSpeedController

"""
This type stub file was generated by pyright.
"""
__all__ = ["DMC60"]
class DMC60(PWMSpeedController):
    """
    Digilent DMC 60 Speed Controller.
    """
    def __init__(self, channel: int) -> None:
        """Constructor.

        :param channel: The PWM channel that the DMC60 is attached to.
                        0-9 are on-board, 10-19 are on the MXP port.

        .. note ::

            The DMC60 uses the following bounds for PWM values. These values
            should work reasonably well for most controllers, but if users
            experience issues such as asymmetric behavior around the deadband
            or inability to saturate the controller in either direction,
            calibration is recommended.  The calibration procedure can be
            found in the DMC 60 User Manual available from Digilent.

            - 2.004ms = full "forward"
            - 1.520ms = the "high end" of the deadband range
            - 1.500ms = center of the deadband range (off)
            - 1.480ms = the "low end" of the deadband range
            - 0.997ms = full "reverse"
        """
        ...
    

