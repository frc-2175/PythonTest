"""
This type stub file was generated by pyright.
"""

from ntcore.constants import NT_NOTIFY_IMMEDIATE, NT_NOTIFY_NEW
from typing import Any, Optional

_is_new = NT_NOTIFY_IMMEDIATE | NT_NOTIFY_NEW
class NtCoreApi(object):
    """
        Internal NetworkTables API wrapper
        
        In theory you could create multiple instances of this
        and talk to multiple NT servers or create multiple
        NT servers... though, I don't really know why one
        would want to do this.
    """
    def __init__(self, entry_creator, verbose: bool = ...):
        self.conn_notifier = ...
        self.entry_notifier = ...
        self.rpc_server = ...
        self.storage = ...
        self.dispatcher = ...
        self.ds_client = ...
    
    def stop(self):
        ...
    
    def destroy(self):
        self.ds_client = ...
        self.dispatcher = ...
        self.rpc_server = ...
        self.entry_notifier = ...
        self.entry_notifier = ...
        self.conn_notifier = ...
        self.storage = ...
    
    def _init_table_functions(self):
        self.getEntry = ...
        self.getEntryId = ...
        self.getEntries = ...
        self.getEntryNameById = ...
        self.getEntryTypeById = ...
        self.getEntryValue = ...
        self.setDefaultEntryValue = ...
        self.setDefaultEntryValueById = ...
        self.setEntryValue = ...
        self.setEntryValueById = ...
        self.setEntryTypeValue = ...
        self.setEntryTypeValueById = ...
        self.setEntryFlags = ...
        self.setEntryFlagsById = ...
        self.getEntryFlags = ...
        self.getEntryFlagsById = ...
        self.deleteEntry = ...
        self.deleteEntryById = ...
        self.deleteAllEntries = ...
        self.getEntryInfo = ...
        self.getEntryInfoById = ...
    
    def addEntryListener(self, prefix, callback, flags):
        ...
    
    def addEntryListenerById(self, local_id, callback, flags):
        ...
    
    def addEntryListenerByIdEx(self, fromobj, key, local_id, callback, flags, paramIsNew):
        ...
    
    def createEntryListenerPoller(self):
        ...
    
    def destroyEntryListenerPoller(self, poller_uid):
        ...
    
    def addPolledEntryListener(self, poller_uid, prefix, flags):
        ...
    
    def addPolledEntryListenerById(self, poller_uid, local_id, flags):
        ...
    
    def pollEntryListener(self, poller_uid, timeout: Optional[Any] = ...):
        ...
    
    def cancelPollEntryListener(self, poller_uid):
        ...
    
    def removeEntryListener(self, listener_uid):
        ...
    
    def waitForEntryListenerQueue(self, timeout):
        ...
    
    def addConnectionListener(self, callback, immediate_notify):
        ...
    
    def createConnectionListenerPoller(self):
        ...
    
    def destroyConnectionListenerPoller(self, poller_uid):
        ...
    
    def addPolledConnectionListener(self, poller_uid, immediate_notify):
        ...
    
    def pollConnectionListener(self, poller_uid, timeout: Optional[Any] = ...):
        ...
    
    def cancelPollConnectionListener(self, poller_uid):
        ...
    
    def removeConnectionListener(self, listener_uid):
        ...
    
    def waitForConnectionListenerQueue(self, timeout):
        ...
    
    def setNetworkIdentity(self, name):
        ...
    
    def getNetworkMode(self):
        ...
    
    def startTestMode(self, is_server):
        ...
    
    def startServer(self, persist_filename, listen_address, port):
        ...
    
    def stopServer(self):
        ...
    
    def startClient(self):
        ...
    
    def stopClient(self):
        ...
    
    def setServer(self, server_or_servers):
        ...
    
    def setServerTeam(self, teamNumber, port):
        ...
    
    def startDSClient(self, port):
        ...
    
    def stopDSClient(self):
        ...
    
    def setUpdateRate(self, interval):
        ...
    
    def flush(self):
        ...
    
    def getRemoteAddress(self):
        ...
    
    def getIsConnected(self):
        ...
    
    def setVerboseLogging(self, verbose):
        ...
    
    def savePersistent(self, filename):
        ...
    
    def loadPersistent(self, filename):
        ...
    
    def saveEntries(self, filename, prefix):
        ...
    
    def loadEntries(self, filename, prefix):
        ...
    


