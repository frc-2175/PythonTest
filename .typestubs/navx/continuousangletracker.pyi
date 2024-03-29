"""
This type stub file was generated by pyright.
"""

class ContinuousAngleTracker:
    def __init__(self):
        self.angleAdjust = ...
        self.lock = ...
    
    def _init(self):
        self.gyro_prevVal = ...
        self.ctrRollOver = ...
        self.fFirstUse = ...
        self.last_yaw_angle = ...
        self.curr_yaw_angle = ...
    
    def nextAngle(self, newAngle):
        ...
    
    def reset(self):
        """Invoked (internally) whenever yaw reset occurs."""
        ...
    
    def getAngle(self):
        ...
    
    def setAngleAdjustment(self, adjustment):
        self.angleAdjust = ...
    
    def getAngleAdjustment(self):
        ...
    
    def getRate(self):
        ...
    


