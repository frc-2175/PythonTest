"""
This type stub file was generated by pyright.
"""

import enum

class ErrorCode(enum.IntEnum):
    OK = ...
    OKAY = ...
    CAN_MSG_STALE = ...
    CAN_TX_FULL = ...
    TxFailed = ...
    InvalidParamValue = ...
    CAN_INVALID_PARAM = ...
    RxTimeout = ...
    CAN_MSG_NOT_FOUND = ...
    TxTimeout = ...
    CAN_NO_MORE_TX_JOBS = ...
    UnexpectedArbId = ...
    CAN_NO_SESSIONS_AVAIL = ...
    BufferFull = ...
    CAN_OVERFLOW = ...
    SensorNotPresent = ...
    FirmwareTooOld = ...
    CouldNotChangePeriod = ...
    BufferFailure = ...
    FirwmwareNonFRC = ...
    GeneralError = ...
    GENERAL_ERROR = ...
    SIG_NOT_UPDATED = ...
    SigNotUpdated = ...
    NotAllPIDValuesUpdated = ...
    GEN_PORT_ERROR = ...
    PORT_MODULE_TYPE_MISMATCH = ...
    GEN_MODULE_ERROR = ...
    MODULE_NOT_INIT_SET_ERROR = ...
    MODULE_NOT_INIT_GET_ERROR = ...
    WheelRadiusTooSmall = ...
    TicksPerRevZero = ...
    DistanceBetweenWheelsTooSmall = ...
    GainsAreNotSet = ...
    WrongRemoteLimitSwitchSource = ...
    IncompatibleMode = ...
    InvalidHandle = ...
    FeatureRequiresHigherFirm = ...
    MotorControllerFeatureRequiresHigherFirm = ...
    TalonFeatureRequiresHigherFirm = ...
    ConfigFactoryDefaultRequiresHigherFirm = ...
    ConfigMotionSCurveRequiresHigherFirm = ...
    LibraryCouldNotBeLoaded = ...
    MissingRoutineInLibrary = ...
    ResourceNotAvailable = ...
    PulseWidthSensorNotPresent = ...
    GeneralWarning = ...
    FeatureNotSupported = ...
    NotImplemented = ...
    FirmVersionCouldNotBeRetrieved = ...
    FeaturesNotAvailableYet = ...
    ControlModeNotValid = ...
    ControlModeNotSupportedYet = ...
    CascadedPIDNotSupporteYet = ...
    AuxiliaryPIDNotSupportedYet = ...
    RemoteSensorsNotSupportedYet = ...
    MotProfFirmThreshold = ...
    MotProfFirmThreshold2 = ...


class ParamEnum(enum.IntEnum):
    eOnBoot_BrakeMode = ...
    eQuadFilterEn = ...
    eQuadIdxPolarity = ...
    eMotionProfileHasUnderrunErr = ...
    eMotionProfileTrajectoryPointDurationMs = ...
    eMotionProfileTrajectoryInterpolDis = ...
    eStatusFramePeriod = ...
    eOpenloopRamp = ...
    eClosedloopRamp = ...
    eNeutralDeadband = ...
    ePeakPosOutput = ...
    eNominalPosOutput = ...
    ePeakNegOutput = ...
    eNominalNegOutput = ...
    eProfileParamSlot_P = ...
    eProfileParamSlot_I = ...
    eProfileParamSlot_D = ...
    eProfileParamSlot_F = ...
    eProfileParamSlot_IZone = ...
    eProfileParamSlot_AllowableErr = ...
    eProfileParamSlot_MaxIAccum = ...
    eProfileParamSlot_PeakOutput = ...
    eClearPositionOnLimitF = ...
    eClearPositionOnLimitR = ...
    eClearPositionOnQuadIdx = ...
    eClearPosOnLimitF = ...
    eClearPosOnLimitR = ...
    eClearPositionOnIdx = ...
    eSampleVelocityPeriod = ...
    eSampleVelocityWindow = ...
    eFeedbackSensorType = ...
    eSelectedSensorPosition = ...
    eFeedbackNotContinuous = ...
    eRemoteSensorSource = ...
    eRemoteSensorDeviceID = ...
    eSensorTerm = ...
    eRemoteSensorClosedLoopDisableNeutralOnLOS = ...
    ePIDLoopPolarity = ...
    ePIDLoopPeriod = ...
    eSelectedSensorCoefficient = ...
    eForwardSoftLimitThreshold = ...
    eReverseSoftLimitThreshold = ...
    eForwardSoftLimitEnable = ...
    eReverseSoftLimitEnable = ...
    eNominalBatteryVoltage = ...
    eBatteryVoltageFilterSize = ...
    eContinuousCurrentLimitAmps = ...
    ePeakCurrentLimitMs = ...
    ePeakCurrentLimitAmps = ...
    eClosedLoopIAccum = ...
    eCustomParam = ...
    eStickyFaults = ...
    eAnalogPosition = ...
    eQuadraturePosition = ...
    ePulseWidthPosition = ...
    eMotMag_Accel = ...
    eMotMag_VelCruise = ...
    eMotMag_SCurveLevel = ...
    eLimitSwitchSource = ...
    eLimitSwitchNormClosedAndDis = ...
    eLimitSwitchDisableNeutralOnLOS = ...
    eLimitSwitchRemoteDevID = ...
    eSoftLimitDisableNeutralOnLOS = ...
    ePulseWidthPeriod_EdgesPerRot = ...
    ePulseWidthPeriod_FilterWindowSz = ...
    eYawOffset = ...
    eCompassOffset = ...
    eBetaGain = ...
    eEnableCompassFusion = ...
    eGyroNoMotionCal = ...
    eEnterCalibration = ...
    eFusedHeadingOffset = ...
    eStatusFrameRate = ...
    eAccumZ = ...
    eTempCompDisable = ...
    eMotionMeas_tap_threshX = ...
    eMotionMeas_tap_threshY = ...
    eMotionMeas_tap_threshZ = ...
    eMotionMeas_tap_count = ...
    eMotionMeas_tap_time = ...
    eMotionMeas_tap_time_multi = ...
    eMotionMeas_shake_reject_thresh = ...
    eMotionMeas_shake_reject_time = ...
    eMotionMeas_shake_reject_timeout = ...
    eDefaultConfig = ...


class CANifierControlFrame(enum.IntEnum):
    CANifier_Control_1_General = ...
    CANifier_Control_2_PwmOutput = ...


class CANifierStatusFrame(enum.IntEnum):
    Status_1_General = ...
    Status_2_General = ...
    Status_3_PwmInputs0 = ...
    Status_4_PwmInputs1 = ...
    Status_5_PwmInputs2 = ...
    Status_6_PwmInputs3 = ...
    Status_8_Misc = ...


class GeneralPin(enum.IntEnum):
    QUAD_IDX = ...
    QUAD_B = ...
    QUAD_A = ...
    LIMR = ...
    LIMF = ...
    SDA = ...
    SCL = ...
    SPI_CS = ...
    SPI_MISO_PWM2P = ...
    SPI_MOSI_PWM1P = ...
    SPI_CLK_PWM0P = ...


class SetValueMotionProfile(enum.IntEnum):
    Disable = ...
    Enable = ...
    Hold = ...


class ControlFrame(enum.IntEnum):
    Control_3_General = ...
    Control_4_Advanced = ...
    Control_6_MotProfAddTrajPoint = ...


class ControlFrameEnhanced(enum.IntEnum):
    Control_3_General = ...
    Control_4_Advanced = ...
    Control_5_FeedbackOutputOverride = ...
    Control_6_MotProfAddTrajPoint = ...


class ControlMode(enum.IntEnum):
    PercentOutput = ...
    Position = ...
    Velocity = ...
    Current = ...
    Follower = ...
    MotionProfile = ...
    MotionMagic = ...
    MotionProfileArc = ...
    Disabled = ...


class DemandType(enum.IntEnum):
    Neutral = ...
    AuxPID = ...
    ArbitraryFeedForward = ...


class FeedbackDevice(enum.IntEnum):
    QuadEncoder = ...
    Analog = ...
    Tachometer = ...
    PulseWidthEncodedPosition = ...
    SensorSum = ...
    SensorDifference = ...
    RemoteSensor0 = ...
    RemoteSensor1 = ...
    SoftwareEmulatedSensor = ...
    CTRE_MagEncoder_Absolute = ...
    CTRE_MagEncoder_Relative = ...


class RemoteFeedbackDevice(enum.IntEnum):
    FactoryDefaultOff = ...
    SensorSum = ...
    SensorDifference = ...
    RemoteSensor0 = ...
    RemoteSensor1 = ...
    SoftwareEmulatedSensor = ...


class FollowerType(enum.IntEnum):
    PercentOutput = ...
    AuxOutput1 = ...


class InvertType(enum.IntEnum):
    None_ = ...
    InvertMotorOutput = ...
    FollowMaster = ...
    OpposeMaster = ...


class LimitSwitchSource(enum.IntEnum):
    FeedbackConnector = ...
    RemoteTalonSRX = ...
    RemoteCANifier = ...
    Deactivated = ...


class RemoteLimitSwitchSource(enum.IntEnum):
    FactoryDefaultOff = ...
    RemoteTalonSRX = ...
    RemoteCANifier = ...
    Deactivated = ...


class LimitSwitchNormal(enum.IntEnum):
    NormallyOpen = ...
    NormallyClosed = ...
    Disabled = ...


class NeutralMode(enum.IntEnum):
    EEPROMSetting = ...
    Coast = ...
    Brake = ...


class RemoteSensorSource(enum.IntEnum):
    Off = ...
    TalonSRX_SelectedSensor = ...
    Pigeon_Yaw = ...
    Pigeon_Pitch = ...
    Pigeon_Roll = ...
    CANifier_Quadrature = ...
    CANifier_PWMInput0 = ...
    CANifier_PWMInput1 = ...
    CANifier_PWMInput2 = ...
    CANifier_PWMInput3 = ...
    GadgeteerPigeon_Yaw = ...
    GadgeteerPigeon_Pitch = ...
    GadgeteerPigeon_Roll = ...


class SensorTerm(enum.IntEnum):
    Sum0 = ...
    Sum1 = ...
    Diff0 = ...
    Diff1 = ...


class StatusFrameEnhanced(enum.IntEnum):
    Status_1_General = ...
    Status_2_Feedback0 = ...
    Status_4_AinTempVbat = ...
    Status_6_Misc = ...
    Status_7_CommStatus = ...
    Status_9_MotProfBuffer = ...
    Status_10_MotionMagic = ...
    Status_10_Targets = ...
    Status_12_Feedback1 = ...
    Status_13_Base_PIDF0 = ...
    Status_14_Turn_PIDF1 = ...
    Status_15_FirmareApiStatus = ...
    Status_17_Targets1 = ...
    Status_3_Quadrature = ...
    Status_8_PulseWidth = ...
    Status_11_UartGadgeteer = ...


class StatusFrame(enum.IntEnum):
    Status_1_General = ...
    Status_2_Feedback0 = ...
    Status_4_AinTempVbat = ...
    Status_6_Misc = ...
    Status_7_CommStatus = ...
    Status_9_MotProfBuffer = ...
    Status_10_MotionMagic = ...
    Status_10_Targets = ...
    Status_12_Feedback1 = ...
    Status_13_Base_PIDF0 = ...
    Status_14_Turn_PIDF1 = ...
    Status_15_FirmareApiStatus = ...
    Status_17_Targets1 = ...


class VelocityMeasPeriod(enum.IntEnum):
    Period_1Ms = ...
    Period_2Ms = ...
    Period_5Ms = ...
    Period_10Ms = ...
    Period_20Ms = ...
    Period_25Ms = ...
    Period_50Ms = ...
    Period_100Ms = ...


class PigeonIMU_ControlFrame(enum.IntEnum):
    CondStatus_Control_1 = ...


class PigeonIMU_StatusFrame(enum.IntEnum):
    CondStatus_1_General = ...
    CondStatus_9_SixDeg_YPR = ...
    CondStatus_6_SensorFusion = ...
    CondStatus_11_GyroAccum = ...
    CondStatus_2_GeneralCompass = ...
    CondStatus_3_GeneralAccel = ...
    CondStatus_10_SixDeg_Quat = ...
    RawStatus_4_Mag = ...
    BiasedStatus_2_Gyro = ...
    BiasedStatus_4_Mag = ...
    BiasedStatus_6_Accel = ...


