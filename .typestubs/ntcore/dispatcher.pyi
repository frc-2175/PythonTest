"""
This type stub file was generated by pyright.
"""

import logging

logger = logging.getLogger("nt")
class Dispatcher(object):
    def __init__(self, storage, conn_notifier, verbose: bool = ...):
        self.m_verbose = ...
        self.m_storage = ...
        self.m_notifier = ...
        self.m_networkMode = ...
        self.m_persist_filename = ...
        self.m_server_acceptor = ...
        self.m_client_connector_override = ...
        self.m_client_connector = ...
        self.m_connections_uid = ...
        self.m_default_proto = ...
        self.m_user_mutex = ...
        self.m_connections = ...
        self.m_identity = ...
        self.m_active = ...
        self.m_update_rate = ...
        self.m_flush_mutex = ...
        self.m_flush_cv = ...
        self.m_last_flush = ...
        self.m_do_flush = ...
        self.m_reconnect_cv = ...
        self.m_reconnect_proto_rev = ...
        self.m_do_reconnect = ...
    
    def setVerboseLogging(self, verbose):
        self.m_verbose = ...
    
    def setServer(self, server_or_servers):
        """
            :param server_or_servers: a tuple of (server, port) or a list of tuples of (server, port)
        """
        ...
    
    def setServerTeam(self, team, port):
        ...
    
    def setServerOverride(self, server, port):
        ...
    
    def clearServerOverride(self):
        ...
    
    def getNetworkMode(self):
        ...
    
    def startTestMode(self, is_server):
        ...
    
    def startServer(self, persist_filename, listen_address, port):
        self.m_networkMode = ...
        self.m_persist_filename = ...
        self.m_server_acceptor = ...
        self.m_dispatch_thread = ...
        self.m_clientserver_thread = ...
    
    def startClient(self):
        self.m_networkMode = ...
        self.m_dispatch_thread = ...
        self.m_clientserver_thread = ...
    
    def stop(self):
        ...
    
    def setUpdateRate(self, interval):
        self.m_update_rate = ...
    
    def setIdentity(self, name):
        ...
    
    def setDefaultProtoRev(self, proto_rev):
        self.m_default_proto = ...
        self.m_reconnect_proto_rev = ...
    
    def flush(self):
        ...
    
    def getConnections(self):
        ...
    
    def isConnected(self):
        ...
    
    def isServer(self):
        ...
    
    def addListener(self, callback, immediate_notify):
        ...
    
    def addPolledListener(self, poller_uid, immediate_notify):
        ...
    
    def _strip_connectors(self, connector):
        ...
    
    def _setConnector(self, connector):
        ...
    
    def _setConnectorOverride(self, connector):
        ...
    
    def _clearConnectorOverride(self):
        ...
    
    def _dispatchWaitFor(self):
        ...
    
    def _dispatchThreadMain(self):
        ...
    
    def _queueOutgoing(self, msg, only, except_):
        ...
    
    def _serverThreadMain(self):
        self.m_networkMode = ...
    
    def _clientThreadMain(self):
        ...
    
    def _clientHandshake(self, conn, get_msg, send_msgs):
        ...
    
    def _serverHandshake(self, conn, get_msg, send_msgs):
        ...
    
    def _clientReconnect(self, proto_rev=...):
        ...
    


