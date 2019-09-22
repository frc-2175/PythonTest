"""
This type stub file was generated by pyright.
"""

from . import data
from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
hal_data = data.hal_data
def notify_new_ds_data():
    """Called when driver station data is modified"""
    ...

def set_autonomous(enabled, game_specific_message: Optional[Any] = ...):
    """Only designed to be called on transition"""
    ...

def set_test_mode(enabled):
    """Only designed to be called on transition"""
    ...

def set_teleop_mode(enabled):
    """Only designed to be called on transition"""
    ...

def set_disabled():
    """Only designed to be called on transition"""
    ...

def set_estop():
    """Only designed to be called on transition"""
    ...

def set_mode(new_mode, new_enabled, **kwargs):
    """
        Calls the appropriate function based on the mode string

        Can be called repeatedly, will only update a mode when it
        changes.

        :param new_mode: auto, test, or teleop
        :param enabled:  True if enabled, False otherwise
    """
    ...
