"""
This type stub file was generated by pyright.
"""

from typing import Optional

"""
This type stub file was generated by pyright.
"""
__all__ = ["Resource"]
class Resource:
    """Tracks resources in the program.
    
    The Resource class is a convenient way of keeping track of allocated
    arbitrary resources in the program. Resources are just indices that
    have an lower and upper bound that are tracked by this class. In the
    library they are used for tracking allocation of hardware channels
    but this is purely arbitrary. The resource class does not do any actual
    allocation, but simply tracks if a given index is currently in use.

    .. not_implemented: restartProgram
    """
    _resource_objects = ...
    _global_resources = ...
    @staticmethod
    def _reset() -> None:
        """
            This clears all resources in the program and calls free() on any
            objects that have a free method.
        """
        ...
    
    @staticmethod
    def _add_global_resource(obj: object) -> None:
        ...
    
    def __init__(self, size: int) -> None:
        """Allocate storage for a new instance of Resource.
        Allocate a bool array of values that will get initialized to
        indicate that no resources have been allocated yet. The indices
        of the resources are 0..size-1.

        :param size: The number of blocks to allocate
        """
        self.numAllocated = ...
    
    def allocate(self, obj: object, index: Optional[int] = ...) -> int:
        """Allocate a resource.

        When index is None or unspecified, a free resource value within the
        range is located and returned after it is marked allocated.
        Otherwise, it is verified unallocated, then returned.

        :param obj: The object requesting the resource.
        :param index: The resource to allocate
        :returns: The index of the allocated block.
        :raises IndexError: If there are no resources available to be
            allocated or the specified index is already used.
        """
        ...
    
    def free(self, index: int) -> None:
        """Force-free an allocated resource.
        After a resource is no longer needed, for example a destructor is
        called for a channel assignment class, free will release the resource
        value so it can be reused somewhere else in the program.

        :param index: The index of the resource to free.
        """
        ...
    


