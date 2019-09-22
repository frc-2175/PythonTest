"""
This type stub file was generated by pyright.
"""

class IMURegisters:
    NAVX_REG_WHOAMI = ...
    NAVX_REG_HW_REV = ...
    NAVX_REG_FW_VER_MAJOR = ...
    NAVX_REG_FW_VER_MINOR = ...
    NAVX_MODEL_NAVX_MXP = ...
    @classmethod
    def model_type(cls, whoami):
        ...
    
    NAVX_REG_UPDATE_RATE_HZ = ...
    NAVX_REG_ACCEL_FSR_G = ...
    NAVX_REG_GYRO_FSR_DPS_L = ...
    NAVX_REG_GYRO_FSR_DPS_H = ...
    NAVX_REG_OP_STATUS = ...
    NAVX_REG_CAL_STATUS = ...
    NAVX_REG_SELFTEST_STATUS = ...
    NAVX_REG_CAPABILITY_FLAGS_L = ...
    NAVX_REG_CAPABILITY_FLAGS_H = ...
    NAVX_REG_SENSOR_STATUS_L = ...
    NAVX_REG_SENSOR_STATUS_H = ...
    NAVX_REG_TIMESTAMP_L_L = ...
    NAVX_REG_TIMESTAMP_L_H = ...
    NAVX_REG_TIMESTAMP_H_L = ...
    NAVX_REG_TIMESTAMP_H_H = ...
    NAVX_REG_YAW_L = ...
    NAVX_REG_YAW_H = ...
    NAVX_REG_ROLL_L = ...
    NAVX_REG_ROLL_H = ...
    NAVX_REG_PITCH_L = ...
    NAVX_REG_PITCH_H = ...
    NAVX_REG_HEADING_L = ...
    NAVX_REG_HEADING_H = ...
    NAVX_REG_FUSED_HEADING_L = ...
    NAVX_REG_FUSED_HEADING_H = ...
    NAVX_REG_ALTITUDE_I_L = ...
    NAVX_REG_ALTITUDE_I_H = ...
    NAVX_REG_ALTITUDE_D_L = ...
    NAVX_REG_ALTITUDE_D_H = ...
    NAVX_REG_LINEAR_ACC_X_L = ...
    NAVX_REG_LINEAR_ACC_X_H = ...
    NAVX_REG_LINEAR_ACC_Y_L = ...
    NAVX_REG_LINEAR_ACC_Y_H = ...
    NAVX_REG_LINEAR_ACC_Z_L = ...
    NAVX_REG_LINEAR_ACC_Z_H = ...
    NAVX_REG_QUAT_W_L = ...
    NAVX_REG_QUAT_W_H = ...
    NAVX_REG_QUAT_X_L = ...
    NAVX_REG_QUAT_X_H = ...
    NAVX_REG_QUAT_Y_L = ...
    NAVX_REG_QUAT_Y_H = ...
    NAVX_REG_QUAT_Z_L = ...
    NAVX_REG_QUAT_Z_H = ...
    NAVX_REG_MPU_TEMP_C_L = ...
    NAVX_REG_MPU_TEMP_C_H = ...
    NAVX_REG_GYRO_X_L = ...
    NAVX_REG_GYRO_X_H = ...
    NAVX_REG_GYRO_Y_L = ...
    NAVX_REG_GYRO_Y_H = ...
    NAVX_REG_GYRO_Z_L = ...
    NAVX_REG_GYRO_Z_H = ...
    NAVX_REG_ACC_X_L = ...
    NAVX_REG_ACC_X_H = ...
    NAVX_REG_ACC_Y_L = ...
    NAVX_REG_ACC_Y_H = ...
    NAVX_REG_ACC_Z_L = ...
    NAVX_REG_ACC_Z_H = ...
    NAVX_REG_MAG_X_L = ...
    NAVX_REG_MAG_X_H = ...
    NAVX_REG_MAG_Y_L = ...
    NAVX_REG_MAG_Y_H = ...
    NAVX_REG_MAG_Z_L = ...
    NAVX_REG_MAG_Z_H = ...
    NAVX_REG_PRESSURE_IL = ...
    NAVX_REG_PRESSURE_IH = ...
    NAVX_REG_PRESSURE_DL = ...
    NAVX_REG_PRESSURE_DH = ...
    NAVX_REG_PRESSURE_TEMP_L = ...
    NAVX_REG_PRESSURE_TEMP_H = ...
    NAVX_REG_YAW_OFFSET_L = ...
    NAVX_REG_YAW_OFFSET_H = ...
    NAVX_REG_QUAT_OFFSET_W_L = ...
    NAVX_REG_QUAT_OFFSET_W_H = ...
    NAVX_REG_QUAT_OFFSET_X_L = ...
    NAVX_REG_QUAT_OFFSET_X_H = ...
    NAVX_REG_QUAT_OFFSET_Y_L = ...
    NAVX_REG_QUAT_OFFSET_Y_H = ...
    NAVX_REG_QUAT_OFFSET_Z_L = ...
    NAVX_REG_QUAT_OFFSET_Z_H = ...
    NAVX_REG_INTEGRATION_CTL = ...
    NAVX_REG_PAD_UNUSED = ...
    NAVX_REG_VEL_X_I_L = ...
    NAVX_REG_VEL_X_I_H = ...
    NAVX_REG_VEL_X_D_L = ...
    NAVX_REG_VEL_X_D_H = ...
    NAVX_REG_VEL_Y_I_L = ...
    NAVX_REG_VEL_Y_I_H = ...
    NAVX_REG_VEL_Y_D_L = ...
    NAVX_REG_VEL_Y_D_H = ...
    NAVX_REG_VEL_Z_I_L = ...
    NAVX_REG_VEL_Z_I_H = ...
    NAVX_REG_VEL_Z_D_L = ...
    NAVX_REG_VEL_Z_D_H = ...
    NAVX_REG_DISP_X_I_L = ...
    NAVX_REG_DISP_X_I_H = ...
    NAVX_REG_DISP_X_D_L = ...
    NAVX_REG_DISP_X_D_H = ...
    NAVX_REG_DISP_Y_I_L = ...
    NAVX_REG_DISP_Y_I_H = ...
    NAVX_REG_DISP_Y_D_L = ...
    NAVX_REG_DISP_Y_D_H = ...
    NAVX_REG_DISP_Z_I_L = ...
    NAVX_REG_DISP_Z_I_H = ...
    NAVX_REG_DISP_Z_D_L = ...
    NAVX_REG_DISP_Z_D_H = ...
    NAVX_REG_LAST = ...

