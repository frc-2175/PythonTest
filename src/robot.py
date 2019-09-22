from ctre import VictorSPX
from ctre import TalonSRX
from navx.ahrs import AHRS
from wpilib import TimedRobot
from wpilib.solenoid import Solenoid

class MyRobot(TimedRobot):
    leftMotor: TalonSRX
    rightMotor: TalonSRX

    mySolenoid = Solenoid(0)

    navx = AHRS.create_i2c()

    def robotInit(self):
        self.leftMotor = VictorSPX(0)
        self.rightMotor = TalonSRX("pizza")
    
    def teleopInit(self):
        self.leftMotor.setSpeed(0.3)
        self.rightMotor.setSpeed(0.3)

        self.mySolenoid.set(True)

        angle = self.navx.getAngle()
