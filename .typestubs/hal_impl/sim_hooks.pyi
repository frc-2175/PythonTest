"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
class SimHooks:
    """
        These are useful hooks to override for simulations.
    
        To use your own hook, set hal_impl.functions.hooks
    """
    def __init__(self):
        self.initialized = ...
    
    def getTime(self):
        ...
    
    def getFPGATime(self):
        ...
    
    def delayMillis(self, ms):
        ...
    
    def delaySeconds(self, s):
        ...
    
    def createCondition(self, lock: Optional[Any] = ...):
        ...
    
    def initializeDriverStation(self):
        ...
    
    def isNewControlData(self):
        ...
    
    def notifyDSData(self):
        ...
    
    def waitForDSData(self, timeout: Optional[Any] = ...):
        ...
    
    def reset(self):
        self.initialized = ...
        self.ds_cond = ...
        self.ds_packets = ...
        self.local = ...
    


