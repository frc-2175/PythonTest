"""
This type stub file was generated by pyright.
"""

import enum
from collections import namedtuple
from ._impl import ParamEnum, PigeonIMU as PigeonImuImpl, PigeonIMU_Faults, PigeonIMU_StickyFaults

__all__ = ["PigeonIMU", "FusionStatus", "GeneralStatus", "PigeonState", "CalibrationMode"]
_FusionStatus = namedtuple("_FusionStatus", ["bIsFusing", "bIsValid", "heading", "lastError"])
class FusionStatus(_FusionStatus):
    """Data object for holding fusion information."""
    def __str__(self):
        ...
    


class CalibrationMode(enum.IntEnum):
    """Various calibration modes supported by Pigeon."""
    BootTareGyroAccel = ...
    Temperature = ...
    Magnetometer12Pt = ...
    Magnetometer360 = ...
    Accelerometer = ...
    Unknown = ...


class PigeonState(enum.IntEnum):
    """Overall state of the Pigeon."""
    NoComm = ...
    Initializing = ...
    Ready = ...
    UserCalibration = ...
    Unknown = ...


_GeneralStatus = namedtuple("_GeneralStatus", ["state", "currentMode", "calibrationError", "bCalIsBooting", "tempC", "upTimeSec", "noMotionBiasCount", "tempCompensationCount", "lastError"])
class GeneralStatus(_GeneralStatus):
    """Data object for status on current calibration and general status.
    
    Pigeon has many calibration modes supported for a variety of uses. The
    modes generally collects and saves persistently information that makes
    the Pigeon signals more accurate. This includes collecting temperature,
    gyro, accelerometer, and compass information.
    
    For FRC use-cases, typically compass and temperature calibration is not
    required.
    
    Additionally when motion driver software in the Pigeon boots, it will
    perform a fast boot calibration to initially bias gyro and setup
    accelerometer.
    
    These modes can be enabled with the EnterCalibration mode.
    
    When a calibration mode is entered, caller can expect...
    
    -
        PigeonState to reset to Initializing and bCalIsBooting is set to true.
        Pigeon LEDs will blink the boot pattern. This is similar to the normal
        boot cal, however it can an additional ~30 seconds since calibration
        generally requires more information. currentMode will reflect the user's
        selected calibration mode.
    
    -
        PigeonState will eventually settle to UserCalibration and Pigeon LEDs
        will show cal specific blink patterns. bCalIsBooting is now false.
    
    -
        Follow the instructions in the Pigeon User Manual to meet the
        calibration specific requirements. When finished calibrationError will
        update with the result. Pigeon will solid-fill LEDs with red (for
        failure) or green (for success) for ~5 seconds. Pigeon then perform
        boot-cal to cleanly apply the newly saved calibration data.

    :param state:
        The current state of the motion driver. This reflects if the sensor
        signals are accurate. Most calibration modes will force Pigeon to
        reinit the motion driver.
    :param currentMode:
        The currently applied calibration mode if state is in UserCalibration
        or if bCalIsBooting is true. Otherwise it holds the last selected
        calibration mode (when calibrationError was updated).
    :param calibrationError:
        The error code for the last calibration mode. Zero represents a
        successful cal (with solid green LEDs at end of cal) and nonzero is a
        failed calibration (with solid red LEDs at end of cal). Different
        calibration
    :param bCalIsBooting:
        After caller requests a calibration mode, pigeon will perform a
        boot-cal before entering the requested mode. During this period, this
        flag is set to true.
    :param tempC:
        Temperature in Celsius
    :param upTimeSec:
        Number of seconds Pigeon has been up (since boot). This register is
        reset on power boot or processor reset. Register is capped at 255
        seconds with no wrap around.
    :param noMotionBiasCount:
        Number of times the Pigeon has automatically rebiased the gyro. This
        counter overflows from 15 -> 0 with no cap.
    :param tempCompensationCount:
        Number of times the Pigeon has temperature compensated the various
        signals. This counter overflows from 15 -> 0 with no cap.
    :param lastError:
        Same as getLastError()
    """
    def __str__(self):
        """
        general string description of current status"""
        ...
    


class PigeonIMU(PigeonImuImpl):
    """Pigeon IMU Class. Class supports communicating over CANbus and over
    ribbon-cable (CAN Talon SRX).
    """
    CalibrationMode = ...
    ControlFrame = ...
    FusionStatus = ...
    ParamEnum = ...
    PigeonState = ...
    StatusFrame = ...
    def __init__(self, *args, **kwargs):
        """
        Arguments can be structured as follows:

        - deviceNumber
        - talonSrx
        
        :param deviceNumber:
            CAN Device Id of Pigeon [0,62]
        :param talonSrx:
            Object for the TalonSRX connected via ribbon cable.

        .. note:: To use this in simulation, you can initialize the device
                  gyro support via one of the following in your physics.py::

            physics_controller.add_device_gyro_channel('pigeon_device_X')
            physics_controller.add_device_gyro_channel('pigeon_srx_X')

        """
        self.generalStatus = ...
        self.fusionStatus = ...
    
    def getGeneralStatus(self) -> GeneralStatus:
        """
        Get the status of the current (or previousley complete) calibration.
        
        :returns: :class:`.GeneralStatus`
            generalstatus.lastError is Error Code generated by function.  0 indicates no error.
        """
        ...
    
    def getFusedHeading(self) -> FusionStatus:
        """
        :param status:
            object reference to fill with fusion status flags.
            Caller may pass null if flags are not needed.
        :returns: :class:`.FusionStatus`
        """
        ...
    
    def getFaults(self) -> PigeonIMU_Faults:
        """
        Gets the fault status

        :returns: (error code, :class:`.PigeonIMU_Faults`)
            Error Code generated by function. 0 indicates no error.
        """
        ...
    
    def getStickyFaults(self) -> PigeonIMU_StickyFaults:
        """
        Gets the sticky fault status

        :returns: (error code, :class:`.PigeonIMU_StickyFaults`)
            Error Code generated by function. 0 indicates no error.
        """
        ...
    
    def getDeviceID(self) -> int:
        """:returns: The Device Number"""
        ...
    


