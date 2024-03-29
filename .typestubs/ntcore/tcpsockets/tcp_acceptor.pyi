"""
This type stub file was generated by pyright.
"""

import logging
from typing import Any, Optional

logger = logging.getLogger("nt")
class TcpAcceptor(object):
    def __init__(self, port, address):
        self.lock = ...
        self.m_lsd = ...
        self.m_port = ...
        self.m_address = ...
        self.m_listening = ...
        self.m_shutdown = ...
    
    def waitForStart(self, timeout: Optional[Any] = ...):
        ...
    
    def close(self):
        ...
    
    def start(self):
        ...
    
    def shutdown(self):
        ...
    
    def accept(self):
        ...
    


