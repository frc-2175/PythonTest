"""
This type stub file was generated by pyright.
"""

NT_UNASSIGNED = b'\x00'
NT_BOOLEAN = b'\x01'
NT_DOUBLE = b'\x02'
NT_STRING = b'\x04'
NT_RAW = b'\x08'
NT_BOOLEAN_ARRAY = b'\x10'
NT_DOUBLE_ARRAY = b'\x20'
NT_STRING_ARRAY = b'\x40'
NT_RPC = b'\x80'
NT_VTYPE2RAW = { NT_BOOLEAN: b'\x00',NT_DOUBLE: b'\x01',NT_STRING: b'\x02',NT_RAW: b'\x03',NT_BOOLEAN_ARRAY: b'\x10',NT_DOUBLE_ARRAY: b'\x11',NT_STRING_ARRAY: b'\x12',NT_RPC: b'\x20' }
NT_RAW2VTYPE = { v: k for (k, v) in NT_VTYPE2RAW.items() }
NT_NOTIFY_NONE = 0
NT_NOTIFY_IMMEDIATE = 1
NT_NOTIFY_LOCAL = 2
NT_NOTIFY_NEW = 4
NT_NOTIFY_DELETE = 8
NT_NOTIFY_UPDATE = 16
NT_NOTIFY_FLAGS = 32
NT_NET_MODE_NONE = 0
NT_NET_MODE_SERVER = 1
NT_NET_MODE_CLIENT = 2
NT_NET_MODE_STARTING = 4
NT_NET_MODE_FAILURE = 8
NT_NET_MODE_TEST = 16
NT_PERSISTENT = 1
kKeepAlive = b'\x00'
kClientHello = b'\x01'
kProtoUnsup = b'\x02'
kServerHelloDone = b'\x03'
kServerHello = b'\x04'
kClientHelloDone = b'\x05'
kEntryAssign = b'\x10'
kEntryUpdate = b'\x11'
kFlagsUpdate = b'\x12'
kEntryDelete = b'\x13'
kClearEntries = b'\x14'
kExecuteRpc = b'\x20'
kRpcResponse = b'\x21'
kClearAllMagic = 3496784506
_msgtypes = { kKeepAlive: 'kKeepAlive',kClientHello: 'kClientHello',kProtoUnsup: 'kProtoUnsup',kServerHelloDone: 'kServerHelloDone',kServerHello: 'kServerHello',kClientHelloDone: 'kClientHelloDone',kEntryAssign: 'kEntryAssign',kEntryUpdate: 'kEntryUpdate',kFlagsUpdate: 'kFlagsUpdate',kEntryDelete: 'kEntryDelete',kClearEntries: 'kClearEntries',kExecuteRpc: 'kExecuteRpc',kRpcResponse: 'kRpcResponse' }
def msgtype_str(msgtype):
    ...

NT_DEFAULT_PORT = 1735
