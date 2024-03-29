"""
This type stub file was generated by pyright.
"""

import logging
from collections import namedtuple
from .callback_manager import CallbackManager, CallbackThread

logger = logging.getLogger("nt")
_RpcListenerData = namedtuple("RpcListenerData", ["callback", "poller_uid"])
_RpcCall = namedtuple("RpcCall", ["local_id", "call_uid", "name", "params", "conn_info", "send_response"])
class RpcServerThread(CallbackThread):
    def __init__(self):
        self.m_response_map = ...
    
    def matches(self, listener, data):
        ...
    
    def setListener(self, data, listener_uid):
        ...
    
    def doCallback(self, callback, data):
        ...
    


class RpcServer(CallbackManager):
    THREAD_CLASS = ...
    def add(self, callback):
        ...
    
    def addPolled(self, poller_uid):
        ...
    
    def removeRpc(self, rpc_uid):
        ...
    
    def processRpc(self, local_id, call_uid, name, params, conn_info, send_response, rpc_uid):
        ...
    
    def postRpcResponse(self, local_id, call_uid, result):
        ...
    
    def start(self):
        ...
    


