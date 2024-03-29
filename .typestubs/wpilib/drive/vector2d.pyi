"""
This type stub file was generated by pyright.
"""

"""
This type stub file was generated by pyright.
"""
__all__ = ["Vector2d"]
class Vector2d:
    """This is a 2D vector struct that supports basic operations"""
    def __init__(self, x: float = ..., y: float = ...) -> None:
        """Construct a 2D vector

        :param x: x component of the vector
        :param y: y component of the vector
        """
        self.x = ...
        self.y = ...
    
    def rotate(self, angle: float) -> None:
        """Rotate a vector in Cartesian space.

        :param angle: Angle in degrees by which to rotate vector counter-clockwise
        """
        self.x = ...
        self.y = ...
    
    def dot(self, vec: Vector2d) -> float:
        """Returns dot product of this vector and argument

        :param vec: Vector with which to perform dot product
        """
        ...
    
    def magnitude(self) -> float:
        """ Returns magnitude of vector"""
        ...
    
    def scalarProject(self, vec: Vector2d) -> float:
        """Returns scalar projection of this vector onto argument

        :param vec: Vector onto which to project this vector
        :return: scalar projection of this vector onto argument
        """
        ...
    


