"""
    Example file to demonstrate the tools available in `inspect` module.
"""
import math
import inspect
from pprint import pp
from typing import Union


def auto_repr(_self):
    _cls = type(_self).__name__

    sig = inspect.signature(_self.__init__)
    params = sig.parameters

    params_info = []
    for param, _type in params.items():
        annotation = getattr(_type.annotation, '__name__', _type.annotation)
        param_obj = getattr(_self, param)
        params_info.append((param, annotation, param_obj))

    _repr = "{cls}({args})".format(
        cls=_cls,
        args=", ".join(
            f"{p[0]}: {p[1]} = {p[2]}"
            for p in params_info
        )
    )

    return _repr


class Shape:
    """
        Base Shape class.
        This class just defines some abstract methods and the __repr__ for derived classes
    """
    @property
    def area(self):
        return self._area()

    @property
    def perimeter(self):
        return self._perimeter()

    def _area(self):
        return NotImplemented

    def _perimeter(self):
        return NotImplemented

    def __repr__(self):
        return auto_repr(self)


class Circle(Shape):
    """
        Circle class: subclasses Shape
        The class initializer expects a single 'radius' argument of type float or int
        This provides 'area' and 'perimeter' properties
    """
    def __init__(self, radius: float = 0.0):
        assert isinstance(radius, (float, int)), "TypeError: 'radius' should be a 'float' value"
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    def _area(self):
        return math.pi * self.radius ** 2

    def _perimeter(self):
        return math.pi * self.radius * 2


class Rectangle(Shape):
    """
        Rectangle class: subclasses Shape
        The class initializer expects 'length' and 'breadth' arguments of type float or int
        This provides 'area' and 'perimeter' properties
    """
    def __init__(self, length: float = 0.0, breadth: float = 0.0):
        assert isinstance(length, (float, int)), "TypeError: 'length' should be a 'float' value"
        assert isinstance(breadth, (float, int)), "TypeError: 'breadth' should be a 'float' value"
        self._length = length
        self._breadth = breadth

    @property
    def length(self):
        return self._length

    @property
    def breadth(self):
        return self._breadth

    def _area(self):
        return self.length * self.breadth

    def _perimeter(self):
        return 2 * (self.length + self.breadth)


class Square(Rectangle):
    """
        Square class: subclasses Rectangle
        The class initializer expects a single 'side' argument of type float or int
        This provides 'area' and 'perimeter' properties
    """
    def __init__(self, side: Union[float, int] = 0.0):
        assert isinstance(side, (float, int)), "TypeError: 'side' should be a 'float' value"
        super().__init__(length=side, breadth=side)
        self._side = side

    @property
    def side(self):
        return self._side


def inspection():
    inst_shape = Shape()
    inst_circle = Circle(radius=42.0)
    inst_rectangle = Rectangle(length=round(math.pi, 2), breadth=round(math.e, 2))
    inst_square = Square(side=round(math.tau, 2))

    print("Inspection: ")
    print()
    print(f"{inspect.isfunction(auto_repr) = }")
    print(f"{inspect.isfunction(inst_shape.area) = }")
    print(f"{inspect.isfunction(inst_shape._area) = }")
    print()
    print(f"{inspect.ismethod(auto_repr) = }")
    print(f"{inspect.ismethod(inst_shape.area) = }")
    print(f"{inspect.ismethod(inst_shape._area) = }")
    print()
    print(f"{inspect.isclass(Circle) = }")
    print(f"{inspect.isclass(Square) = }")
    print(f"{inspect.isclass(inst_rectangle) = }")
    print()
    print(f"{inspect.isbuiltin(repr) = }")
    print(f"{inspect.isbuiltin(math.sin) = }")
    print(f"{inspect.isbuiltin(auto_repr) = }")
    print()
    print(f"inspect.getmembers(Rectangle) = ", end='')
    pp(inspect.getmembers(Rectangle))
    print(f"\ninspect.getmembers(inst_square) = ", end='')
    pp(inspect.getmembers(inst_square))
    print()
    print(f"{inspect.getmro(Square) = }")
    print()
    print(f"{inspect.getclasstree([Square]) = }")
    print()
    print(f"{inspect.getdoc(inst_shape) = !s}\n")
    print(f"{inspect.getdoc(inst_circle) = !s}\n")
    print(f"{inspect.getdoc(inst_rectangle) = !s}\n")
    print(f"{inspect.getdoc(inst_square) = !s}")
    print()
    print(f"{inspect.isgenerator(list()) = }")
    print(f"{inspect.isgeneratorfunction(map(int, list([56.8, 98.42]))) = }")
    print()
    print(f"{inspect.ismemberdescriptor(inst_circle.area) = }")
    print(f"{inspect.isdatadescriptor(inst_circle.area) = }")
    print(f"{inspect.isgetsetdescriptor(inst_circle.area) = }")
    print(f"{inspect.ismethoddescriptor(inst_circle.area) = }")
    print()


if __name__ == '__main__':
    inspection()

