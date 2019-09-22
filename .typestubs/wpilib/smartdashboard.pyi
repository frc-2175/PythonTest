"""
This type stub file was generated by pyright.
"""

from typing import Iterable, List, Tuple, TypeVar, Union
from networktables.entry import NetworkTableEntry
from networktables.networktable import NetworkTable
from .sendable import Sendable

"""
This type stub file was generated by pyright.
"""
T = TypeVar("T")
__all__ = ["SmartDashboard"]
class Data:
    def __init__(self, sendable: Sendable) -> None:
        self.sendable = ...
        self.builder = ...
    


class SmartDashboard:
    """The bridge between robot programs and the SmartDashboard on the laptop

    When a value is put into the SmartDashboard, it pops up on the
    SmartDashboard on the remote host. Users can put values into and get values
    from the SmartDashboard.
    
    These values can also be accessed by a NetworkTables client via the
    'SmartDashboard' table::
    
        from networktables import NetworkTables
        sd = NetworkTables.getTable('SmartDashboard')
        
        # sd.putXXX and sd.getXXX work as expected here
    
    """
    table = ...
    tablesToData = ...
    mutex = ...
    @classmethod
    def _reset(cls) -> None:
        ...
    
    @classmethod
    def getTable(cls) -> NetworkTable:
        ...
    
    @classmethod
    def putData(cls, *args, **kwargs) -> None:
        """
        Maps the specified key (name of the :class:`.Sendable` if not provided) 
        to the specified value in this table.
        The value can be retrieved by calling the get method with a key that
        is equal to the original key.

        Two argument formats are supported: 
        
        - key, data
        - value
        
        :param key: the key (cannot be None)
        :type key: str
        :param data: the value
        :type data: :class:`.Sendable`
        :param value: the value
        :type value: :class:`.Sendable`
        """
        ...
    
    @classmethod
    def getData(cls, key: str) -> Sendable:
        """Returns the value at the specified key.
        
        :param key: the key

        :returns: the value
        
        :raises: :exc:`KeyError` if the key doesn't exist
        """
        ...
    
    @classmethod
    def getEntry(cls, key: str) -> NetworkTableEntry:
        """Gets the entry for the specified key.
        
        :param key: the key name
        """
        ...
    
    @classmethod
    def containsKey(cls, key: str) -> bool:
        """Checks the table and tells if it contains the specified key.

        :param key: key the key to search for
        
        :returns: true if the table as a value assigned to the given key
        """
        ...
    
    @classmethod
    def getKeys(cls, types: int = ...) -> List[str]:
        """Get the keys stored in the SmartDashboard table of NetworkTables.

        :param types: bitmask of types; 0 is treated as a "don't care".
        
        :returns: keys currently in the table
        """
        ...
    
    @classmethod
    def setPersistent(cls, key: str) -> None:
        """Makes a key's value persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
        ...
    
    @classmethod
    def clearPersistent(cls, key: str) -> None:
        """Stop making a key's value persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
        ...
    
    @classmethod
    def isPersistent(cls, key: str) -> bool:
        """Returns whether the value is persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        
        :returns: True if the value is persistent.
        """
        ...
    
    @classmethod
    def setFlags(cls, key: str, flags: int) -> None:
        """Sets flags on the specified key in this table. The key can
        not be null.

        :param key: the key name
        :param flags: the flags to set (bitmask)
        """
        ...
    
    @classmethod
    def clearFlags(cls, key: str, flags: int) -> None:
        """Clears flags on the specified key in this table. The key can
        not be null.

        :param key: the key name
        :param flags: the flags to clear (bitmask)
        """
        ...
    
    @classmethod
    def getFlags(cls, key: str) -> int:
        """ Returns the flags for the specified key.

        :param key: the key name
        
        :returns: the flags, or 0 if the key is not defined
        """
        ...
    
    @classmethod
    def delete(cls, key: str) -> None:
        """Deletes the specified key in this table. The key can
        not be null.

        :param key: the key name
        """
        ...
    
    @classmethod
    def putBoolean(cls, key: str, value: bool) -> bool:
        """Put a boolean in the table.

        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :return False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultBoolean(cls, key: str, defaultValue: bool) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getBoolean(cls, key: str, defaultValue: T) -> Union[T, bool]:
        """Returns the boolean the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putNumber(cls, key: str, value: float) -> bool:
        """Put a number in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultNumber(cls, key: str, defaultValue: float) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getNumber(cls, key: str, defaultValue: T) -> Union[T, float]:
        """Returns the number the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putString(cls, key: str, value: str) -> bool:
        """Put a string in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultString(cls, key: str, defaultValue: str) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getString(cls, key: str, defaultValue: T) -> Union[T, str]:
        """Returns the string the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putBooleanArray(cls, key: str, value: Iterable[bool]) -> bool:
        """Put a boolean array in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultBooleanArray(cls, key: str, defaultValue: Iterable[bool]) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getBooleanArray(cls, key: str, defaultValue: T) -> Union[T, Tuple[bool, ...]]:
        """Returns the boolean array the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putNumberArray(cls, key: str, value: Iterable[float]) -> bool:
        """Put a number array in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultNumberArray(cls, key: str, defaultValue: Iterable[float]) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getNumberArray(cls, key: str, defaultValue: T) -> Union[T, Tuple[float, ...]]:
        """Returns the number array the key maps to. If the key does not exist or is of
        different type, it will return the default value.

        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putStringArray(cls, key: str, value: Iterable[str]) -> bool:
        """Put a string array in the table
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned

        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultStringArray(cls, key: str, defaultValue: Iterable[str]) -> bool:
        """If the key doesn't currently exist, then the specified value will
        be assigned to the key.
        
        :param key: the key to be assigned to
        :param defaultValue: the default value to set if key doesn't exist.

        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getStringArray(cls, key: str, defaultValue: T) -> Union[T, Tuple[str, ...]]:
        """Returns the string array the key maps to. If the key does not exist or is
        of different type, it will return the default value.
        
        :param key: the key to look up
        :param defaultValue: the value to be returned if no value is found

        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def putRaw(cls, key: str, value: bytes) -> bool:
        """Put a raw value (byte array) in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        ...
    
    @classmethod
    def setDefaultRaw(cls, key: str, defaultValue: bytes) -> bool:
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        ...
    
    @classmethod
    def getRaw(cls, key: str, defaultValue: T) -> Union[T, bytes]:
        """Returns the raw value (byte array) the key maps to. If the key does not exist or is of
        different type, it will return the default value.

        :param key: the key to look up
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        ...
    
    @classmethod
    def updateValues(cls) -> None:
        ...
    


