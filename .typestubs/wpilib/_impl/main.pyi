"""
This type stub file was generated by pyright.
"""

import argparse
from typing import Any, Optional

"""
This type stub file was generated by pyright.
"""
def _log_versions():
    ...

def _enable_faulthandler():
    ...

class _CustomHelpAction(argparse.Action):
    def __init__(self, option_strings, dest=..., default=..., help: Optional[Any] = ...):
        ...
    
    def __call__(self, parser, namespace, values, option_string: Optional[Any] = ...):
        ...
    


def run(robot_class, **kwargs):
    """
        This function gets called in robot.py like so::

            if __name__ == '__main__':
                wpilib.run(MyRobot)

        This function loads available entry points, parses arguments, and
        sets things up specific to RobotPy so that the robot can run. This
        function is used whether the code is running on the roboRIO or
        a simulation.

        :param robot_class: A class that inherits from :class:`.RobotBase`
        :param **kwargs: Keyword arguments that will be passed to the executed entry points
        :returns: This function should never return
    """
    ...
