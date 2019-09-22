"""
This type stub file was generated by pyright.
"""

class StreamEOF(IOError):
    ...


class TCPStream(object):
    def __init__(self, sd, peer_ip, peer_port, sock_type):
        self.m_sd = ...
        self.m_peerIP = ...
        self.m_peerPort = ...
        self.m_rdsock = ...
        self.m_wrsock = ...
        self.close_lock = ...
        self.sock_type = ...
    
    def read(self, size):
        ...
    
    def readline(self):
        ...
    
    def readStruct(self, s):
        ...
    
    def send(self, contents):
        ...
    
    def close(self):
        ...
    
    def getPeerIP(self):
        ...
    
    def getPeerPort(self):
        ...
    
    def setNoDelay(self):
        ...
    
    def _waitForReadEvent(self, timeout):
        ...
    


