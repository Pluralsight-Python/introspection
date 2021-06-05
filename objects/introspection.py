#!/usr/bin/env python3
"""
    This file contains examples of 'object' introspection tools in Python
    - dir(): Lists the name (as a string) of all the attributes of passed object. Note that the methods
    are also attributes
    - getattr(): Get the attribute object by its name (as string)
    - hasattr(): Check if the attribute with given name (as string) exists in the object
    - __name__: To retreive name (as string) of any attribute/object's class, etc.
    - callable(): Check if given object/attribute is a callable.
"""
print()


class Dummy:
    """
        This is a dummy class for demonstrating
        Object Introspection in Python
    """
    cls_attr = 42

    def __init__(self):
        self.inst_attr = 0

    def __repr__(self):
        return f"{self.__class__.__name__}()"


print(f"{dir(int) = }\n")
print(f"{dir(int(42)) = }\n")
print(f"{dir(Dummy) = }\n")
print(f"{dir(Dummy()) = }\n")
print(f"Extra attributes in instance of Dummy: {set(dir(Dummy())) - set(dir(Dummy))}")
print()

if hasattr(Dummy, '__repr__'):
    _repr = getattr(Dummy, '__repr__')
    print(f"{hasattr(Dummy, '__repr__') = }")
    print(f"_repr = {getattr(Dummy, '__repr__') = }")
    print(f"{_repr(Dummy()) = }")
    print()

# Following Python's developmental approach of EAFP (Easier to Ask Forgiveness than Permission) over
# LBYL (Look Before You Leap), it is advised not to use hasattr, hence following is an alternate
# similar way of using 'getattr'

attr = getattr(Dummy, 'cls_attr', 'undefined')
print(f"attr = {getattr(Dummy, 'cls_attr', 'undefined') = }")
print(f"{callable(attr) = }")
print(f"{attr = }")
print(f"{type(attr) = }")
print(f"{type(attr).__name__ = }")
print()

callable_attr = getattr(Dummy, '__str__', 'undefined')
print(f"callable_attr = {getattr(Dummy, '__str__', 'undefined') = }")
print(f"{callable(callable_attr) = }")
print(f"{callable_attr(Dummy()) = }")
print(f"{type(callable_attr) = }")
print(f"{type(callable_attr).__name__ = }")
print()

attr = getattr(Dummy, '__doc__', 'undefined')
print(f"attr = getattr(Dummy, '__doc__', 'undefined')")
print(f"{callable(attr) = }")
print(f"{attr = !s}")
print(f"{type(attr) = }")
print(f"{type(attr).__name__ = }")
print()

