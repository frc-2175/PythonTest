"""
This type stub file was generated by pyright.
"""

from typing import Union
from .digitalsource import DigitalSource
from .encoder import Encoder
from .counter import Counter
from .sendablebuilder import SendableBuilder
from .sendablebase import SendableBase

"""
This type stub file was generated by pyright.
"""
__all__ = ["DigitalGlitchFilter"]
class DigitalGlitchFilter(SendableBase):
    """
    Class to enable glitch filtering on a set of digital inputs.
    This class will manage adding and removing digital inputs from a FPGA glitch
    filter. The filter lets the user configure the time that an input must remain
    high or low before it is classified as high or low.
    """
    mutex = ...
    filterAllocated = ...
    def __init__(self) -> None:
        self.channelIndex = ...
    
    def close(self) -> None:
        ...
    
    @staticmethod
    def _setFilter(input: DigitalSource, channelIndex: int) -> None:
        ...
    
    def add(self, input: Union[DigitalSource, Encoder, Counter]) -> None:
        """
        Assigns the :class:`.DigitalSource`, :class:`.Encoder`, or
        :class:`counter.Counter` to this glitch filter.

        :param input: The object to add
        """
        ...
    
    def remove(self, input: Union[DigitalSource, Encoder, Counter]) -> None:
        """
        Removes this filter from the given input object
        """
        ...
    
    def setPeriodCycles(self, fpga_cycles: int) -> None:
        """
        Sets the number of FPGA cycles that the input must hold steady to pass
        through this glitch filter.

        :param fpga_cycles: The number of FPGA cycles.
        """
        ...
    
    def setPeriodNanoSeconds(self, nanoseconds: float) -> None:
        """
        Sets the number of nanoseconds that the input must hold steady to pass
        through this glitch filter.

        :param nanoseconds: The number of nanoseconds.
        """
        ...
    
    def getPeriodCycles(self) -> int:
        """
        Gets the number of FPGA cycles that the input must hold steady to pass
        through this glitch filter.

        :returns: The number of cycles.
        """
        ...
    
    def getPeriodNanoSeconds(self) -> float:
        """
        Gets the number of nanoseconds that the input must hold steady to pass
        through this glitch filter.

        :returns: The number of nanoseconds.
        """
        ...
    
    def initSendable(self, builder: SendableBuilder) -> None:
        ...
    

