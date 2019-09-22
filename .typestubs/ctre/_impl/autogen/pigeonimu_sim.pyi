"""
This type stub file was generated by pyright.
"""

import typing
from .ctre_sim_enums import ErrorCode

class PigeonIMU:
    def __init__(self):
        self.create_called = ...
    
    def _create2(self, talonDeviceID: int) -> None:
        self.create_called = ...
    
    def _create1(self, deviceNumber: int) -> None:
        self.create_called = ...
    
    def configSetParameter(self, param: int, value: float, subValue: int, ordinal: int, timeoutMs: int = ...) -> ErrorCode:
        '''Sets a parameter. Generally this is not used.

        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:
            Parameter enumeration.
        :param value:
            Value of parameter.
        :param subValue:
            Subvalue for parameter. Maximum value of 255.
        :param ordinal:
            Ordinal of parameter.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def configGetParameter(self, param: int, ordinal: int, timeoutMs: int = ...) -> float:
        '''Gets a parameter. Generally this is not used.

        This can be utilized in

        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:
            Parameter enumeration.
        :param ordinal:
            Ordinal of parameter.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Value of parameter.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def configGetParameter_6(self, param: int, valueToSend: int, ordinal: int, timeoutMs: int = ...) -> typing.Tuple[int, int]:
        ...
    
    def configSetCustomParam(self, newValue: int, paramIndex: int, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/declination/offset
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param newValue:
            Value for custom parameter.
        :param paramIndex:
            Index of custom parameter [0-1].
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def configGetCustomParam(self, paramIndex: int, timoutMs: int) -> int:
        '''Gets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/declination/offset
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param paramIndex:
            Index of custom parameter [0-1].
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Value of the custom param.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def configFactoryDefault(self, timeoutMs: int = ...) -> ErrorCode:
        ...
    
    def setYaw(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the Yaw register to the specified value.

        :param angleDeg: Degree of Yaw [+/- 23040 degrees]
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.

        '''
        ...
    
    def addYaw(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Atomically add to the Yaw register.

        :param angleDeg: Degrees to add to the Yaw register.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.

        '''
        ...
    
    def setYawToCompass(self, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the Yaw register to match the current compass value.

        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setFusedHeading(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the Fused Heading to the specified value.

        :param angleDeg: Degree of heading [+/- 23040 degrees]
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.

        '''
        ...
    
    def addFusedHeading(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Atomically add to the Fused Heading register.

        :param angleDeg: Degrees to add to the Fused Heading register.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.

        '''
        ...
    
    def setFusedHeadingToCompass(self, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the Fused Heading register to match the current compass value.

        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setAccumZAngle(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the AccumZAngle.

        :param angleDeg: Degrees to set AccumZAngle to.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setTemperatureCompensationDisable(self, bTempCompDisable: int, timeoutMs: int = ...) -> ErrorCode:
        '''Disable/Enable Temp compensation. Pigeon has this on/False at boot.

        :param bTempCompDisable: Set to "False" to enable temperature compensation.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.

        '''
        ...
    
    def setCompassDeclination(self, angleDegOffset: float, timeoutMs: int = ...) -> ErrorCode:
        '''Set the declination for compass. Declination is the difference between
        Earth Magnetic north, and the geographic "True North".

        :param angleDegOffset:  Degrees to set Compass Declination to.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setCompassAngle(self, angleDeg: float, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the compass angle. Although compass is absolute [0,360) degrees, the
        continuous compass register holds the wrap-arounds.

        :param angleDeg:
            Degrees to set continuous compass angle to.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def enterCalibrationMode(self, calMode: int, timeoutMs: int = ...) -> ErrorCode:
        '''Enters the Calbration mode.  See the Pigeon IMU documentation for More
        information on Calibration.

        :param calMode: Calibration to execute
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for
            config success and report an error if it times out.
            If zero, no blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def _getGeneralStatus(self) -> typing.Tuple[int, int, int, int, float, int, int, int, int]:
        ...
    
    def getLastError(self) -> ErrorCode:
        '''Call GetLastError() generated by this object.

        Not all functions return an error code but can
        potentially report errors.

        This function can be used to retrieve those error codes.

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def get6dQuaternion(self) -> typing.List[float]:
        '''Get 6d Quaternion data.

        :param wxyz: [w, x, y, z]
        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getYawPitchRoll(self) -> typing.List[float]:
        '''Get Yaw, Pitch, and Roll data.

        :returns: [yaw, pitch, and roll]

        '''
        ...
    
    def getAccumGyro(self) -> typing.List[float]:
        '''Get AccumGyro data.
        AccumGyro is the integrated gyro value on each axis.

        :returns: [x, y, z]

        '''
        ...
    
    def getAbsoluteCompassHeading(self) -> float:
        '''Get the absolute compass heading.

        :returns: compass heading [0,360) degrees.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getCompassHeading(self) -> float:
        '''Get the continuous compass heading.

        :returns:
            continuous compass heading [-23040, 23040) degrees.
            Use SetCompassHeading to modify the wrap-around portion.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getCompassFieldStrength(self) -> float:
        '''Gets the compass' measured magnetic field strength.

        :returns: field strength in Microteslas (uT).


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getTemp(self) -> float:
        '''Gets the temperature of the pigeon.

        :returns: Temperature in ('C)


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getState(self) -> int:
        '''Gets the current Pigeon state

        :returns: PigeonState enum


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getUpTime(self) -> int:
        '''Gets the current Pigeon uptime.

        :returns: How long has Pigeon been running in whole seconds. Value caps at 255.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getRawMagnetometer(self) -> typing.List[int]:
        '''Get Raw Magnetometer data.

        :param rm_xyz: Array to fill with x[0], y[1], and z[2] data.
                       Number is equal to 0.6 microTeslas per unit.

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getBiasedMagnetometer(self) -> typing.List[int]:
        '''Get Biased Magnetometer data.

        :param bm_xyz: Array to fill with x[0], y[1], and z[2] data.
                       Number is equal to 0.6 microTeslas per unit.

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getBiasedAccelerometer(self) -> typing.List[int]:
        '''Get Biased Accelerometer data.

        :param ba_xyz: Array to fill with x[0], y[1], and z[2] data.
                       These are in fixed point notation Q2.14.  e.g. 16384 = 1G

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getRawGyro(self) -> typing.List[float]:
        '''Get Raw Gyro data.

        :param xyz_dps: Array to fill with x[0], y[1], and z[2] data in degrees per second.

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getAccelerometerAngles(self) -> typing.List[float]:
        '''Get Accelerometer tilt angles.

        :param tiltAngles: Array to fill with x[0], y[1], and z[2] angles in degrees.

        :returns: The last ErrorCode generated.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def _getFusedHeading2(self) -> typing.Tuple[int, int, float, int]:
        ...
    
    def _getFusedHeading1(self) -> float:
        ...
    
    def getResetCount(self) -> int:
        ...
    
    def getResetFlags(self) -> int:
        ...
    
    def getFirmwareVersion(self) -> int:
        '''Gets the firmware version of the device.

        :returns:
            param holds the firmware version of the device. Device must be powered
            cycled at least once.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def hasResetOccurred(self) -> bool:
        ''':returns: true iff a reset has occurred since last call.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setLastError(self, value: int) -> ErrorCode:
        ...
    
    def _getFaults(self) -> int:
        ...
    
    def _getStickyFaults(self) -> int:
        ...
    
    def clearStickyFaults(self, timeoutMs: int = ...) -> ErrorCode:
        '''Clears the Sticky Faults

        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setStatusFramePeriod(self, frame: int, periodMs: int, timeoutMs: int = ...) -> ErrorCode:
        '''Sets the period of the given status frame.

        :param statusFrame:
            Frame whose period is to be changed.
        :param periodMs:
            Period in ms for the given frame.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def getStatusFramePeriod(self, frame: int, timeoutMs: int = ...) -> int:
        '''Gets the period of the given status frame.

        :param frame:
            Frame to get the period of.
        :param timeoutMs:
            Timeout value in ms. If nonzero, function will wait for config
            success and report an error if it times out. If zero, no
            blocking or checking is performed.
        :returns: Period of the given status frame.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    
    def setControlFramePeriod(self, frame: int, periodMs: int) -> ErrorCode:
        '''Sets the period of the given control frame.

        :param frame:
            Frame whose period is to be changed.
        :param periodMs:
            Period in ms for the given frame.
        :returns: Error Code generated by function. 0 indicates no error.


        .. note:: This function works on a real robot, but has not yet
                  been implemented in simulation mode. See :ref:`api_support`
                  for more details.

        '''
        ...
    


