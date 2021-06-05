#!/usr/bin/env python3
"""
    This file contains examples of type introspection tools in Python
"""
from pprint import pprint

# 1. type()
print("\n type(): ")
print("=========\n")

i = 42
print(f"{type(i) = }")
s = 'python'
print(f"{type(s) = }")
print()

print(f"{type(int) = }")
print(f"{type(str) = }")
print()


class Dummy:
    pass
print(f"{type(Dummy) = }")
print(f"{type(Dummy()) = }")
print()


obj = Dummy
assert type(obj) == obj.__class__, "type(obj) == obj.__class__"

if 0:
    # This doesn't work
    annotated_only: int
    print(f"{type(annotated_only)=}")
    print()

print(f"{i.__class__ = }")
print(f"{type(i)(89).__class__ = }")
print()

print(f"{type(type('Hello')) = }")
print(f"{type(type(type(type('Hello')))) = }")
print()

print(f"{type(object) = }")
print(f"{object.__class__ = }")
print(f"{object().__class__ = }")
print(f"{object().__class__() = }")
print(f"{type(object().__class__) = }")
print()


# 2. isinstance()
print("\n isinstance()")
print("==============\n")

print(f"{isinstance(42, int) = }")
print(f"{isinstance(i, int) = }")
print(f"{isinstance(s, str) = }")
print(f"{isinstance(int(), int) = }")
print(f"{isinstance(int, int) = }")
print(f"{isinstance(int, object) = }")
print(f"{isinstance(int, type) = }")
print()

print(f"{isinstance(type, object) = }")
print(f"{isinstance(object, type) = }")
print()

print(f"{isinstance({}, (tuple, list, dict)) = }")
print(f"{isinstance({}, (object,)) = }")
print(f"{isinstance({}, (tuple, list, int, str)) = }")
print()

if 0:
    # This doesn't work, because isinstance() expects 2nd arg to be a 'type' or
    # tuple of type objects.
    print(f"{isinstance(int, int()) = }")
    print()


class Base1: pass
class Derived1L1(Base1): pass
class Derived1L2(Derived1L1): pass
class Derived1L3(Derived1L2): pass

print(f"Derived1L3.mro() = ", end='')
pprint(Derived1L3.mro())
print(f"{isinstance(Derived1L3(), Derived1L3) = }")
print(f"{isinstance(Derived1L3(), Derived1L2) = }")
print(f"{isinstance(Derived1L3(), Derived1L1) = }")
print(f"{isinstance(Derived1L3(), Base1) = }")
print(f"{isinstance(Derived1L3, Derived1L2) = }")
print()


class Base2: pass
class Derived2L1(Base2): pass
class Derived3L1(Base2): pass
class Derived4L1(Base2): pass
class DerivedMultipleL2(Derived2L1, Derived3L1, Derived4L1): pass

print(f"DerivedMultipleL2.mro() = ", end='')
pprint(DerivedMultipleL2.mro())
print(f"{isinstance(DerivedMultipleL2(), DerivedMultipleL2) = }")
print(f"{isinstance(DerivedMultipleL2(), Derived2L1) = }")
print(f"{isinstance(DerivedMultipleL2(), Base2) = }")
print()


# 3. issubclass()
print(f"\n issubclass")
print(f"============\n")

print(f"{issubclass(int, object) = }")
print(f"{issubclass(str, object) = }")
print(f"{issubclass(list, dict) = }")
print(f"{issubclass(list, list) = }")
print(f"{issubclass(object, type) = }")
print(f"{issubclass(type, object) = }")
print()

print(f"{Derived1L1.__bases__ = }\n{issubclass(Derived1L1, Base1) = }")
print(f"{Derived1L3.__bases__ = }\n{issubclass(Derived1L3, Base1) = }")
print(f"{Derived2L1.__bases__ = }\n{issubclass(Derived2L1, Base2) = }")
print(f"{issubclass(Derived2L1, Base1) = }")
print()

print(f"{DerivedMultipleL2.__bases__ = }\n{issubclass(DerivedMultipleL2, Base2) = }")
print(f"{issubclass(DerivedMultipleL2, Derived2L1) = }")
print(f"{issubclass(DerivedMultipleL2, Derived3L1) = }")
print(f"{issubclass(DerivedMultipleL2, Derived4L1) = }")
print()

if 0:
    # This doesn't work, issubclass accepts 'class' object as first arg,
    # and 'class' or tuple of classes as 2nd arg.
    print(f"{issubclass(int(), int) = }")
    print(f"{issubclass(list, list()) = }")
    print()

print(f"{issubclass(OSError, (IOError, BaseException, Exception)) = }")
print(f"{issubclass(ConnectionError, (IndexError, ValueError)) = }")
print()


