"""
This type stub file was generated by pyright.
"""

from . import data

"""
This type stub file was generated by pyright.
"""
hal_data = data.hal_data
class I2CSimBase:
    """
        Base class to use for i2c protocol simulators.

        Has all functions that need to be implemented, but throws exceptions
        when data is asked of it. Will throw away set* function data, as most
        low-fidelity simulation will probably not care about such things.
    """
    def initializeI2C(self, port, status):
        self.port = ...
    
    def transactionI2C(self, port, deviceAddress, dataToSend, sendSize, dataReceived, receiveSize):
        """
            Writes data to the I2C device and then reads from it. You can read
            bytes from the ``dataToSend`` parameter. To return data,
            you need to write bytes to the ``data_received`` parameter.
            object.
            
            A simple example of returning 3 bytes might be::
            
                def transactionI2C(self, port, deviceAddress, dataToSend, sendSize, dataReceived, receiveSize):
                    dataReceived[:] = b'123'
                    return len(dataReceived)
            
            :returns: number of bytes returned
        """
        ...
    
    def writeI2C(self, port, deviceAddress, dataToSend, sendSize):
        """:returns: number of bytes written"""
        ...
    
    def readI2C(self, port, deviceAddress, buffer, count):
        """
            Reads data from the I2C device. To return data to your code, you
            need to write bytes to the ``buffer`` parameter. A simple example of
            returning 3 bytes might be::
            
                def readI2C(self, port, deviceAddress, buffer, count):
                    buffer[:] = b'123'
                    return len(buffer)
            
            :returns: number of bytes read
        """
        ...
    
    def closeI2C(self, port):
        ...
    


