"""
This type stub file was generated by pyright.
"""

import logging

logger = logging.getLogger("nt.th")
class SafeThread(object):
    """
        Not exactly the same as wpiutil SafeThread... exists so we don't have
        to duplicate functionality in a lot of places
    """
    _global_indices_lock = ...
    _global_indices = ...
    def __init__(self, target, name, args=...):
        """
            Note: thread is automatically started and daemonized
        """
        self.name = ...
        self.is_alive = ...
        self.join = ...
    
    def join(self, timeout=...):
        ...
    
    def _run(self, target, args):
        ...
    


