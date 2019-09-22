"""
This type stub file was generated by pyright.
"""

from collections import namedtuple
from .callback_manager import CallbackManager, CallbackThread
from typing import Any, Optional

_ConnectionCallback = namedtuple("ConnectionCallback", ["callback", "poller_uid"])
_ConnectionNotification = namedtuple("ConnectionNotification", ["connected", "conn_info"])
class ConnectionNotifierThread(CallbackThread):
    def __init__(self):
        ...
    
    def matches(self, listener, data):
        ...
    
    def setListener(self, data, listener_uid):
        ...
    
    def doCallback(self, callback, data):
        ...
    


class ConnectionNotifier(CallbackManager):
    THREAD_CLASS = ...
    def add(self, callback):
        ...
    
    def addPolled(self, poller_uid):
        ...
    
    def notifyConnection(self, connected, conn_info, only_listener: Optional[Any] = ...):
        ...
    
    def start(self):
        ...
    


