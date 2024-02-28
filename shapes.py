"""Shapes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self._color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    @abstractmethod
    def get_area(self) -> float:
        """Abstract method to get the area of the shape."""
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self._radius = radius

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return pi * self._radius**2

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self._radius}, color: {self.get_color()})"


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self._side = side

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self._side**2

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self._side}, color: {self.get_color()})"


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, length: float, width: float):
        """
        Rectangle constructor.

        The color, length, and width are stored using superclass constructor:
        super().__init__(color)

        The length and width values are stored here.
        """
        super().__init__(color)
        self._length = length
        self._width = width

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Area of the rectangle is length * width.
        """
        return self._length * self._width

    def __repr__(self) -> str:
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Rectangle (l: {length}, w: {width}, color: {color})
        """
        return f"Rectangle (l: {self._length}, w: {self._width}, color: {self.get_color()})"


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self._shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self._shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self._shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = sum(shape.get_area() for shape in self._shapes)
        return total_area

    def get_circles(self) -> list:
        """Return only circles."""
        return [shape for shape in self._shapes if isinstance(shape, Circle)]

    def get_squares(self) -> list:
        """Return only squares."""
        return [shape for shape in self._shapes if isinstance(shape, Square)]

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        return [shape for shape in self._shapes if isinstance(shape, Rectangle)]


# Example Usage:
if __name__ == "__main__":
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    rectangle = Rectangle("green", 5, 8)

    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)

    print(paint.calculate_total_area())  # Output: Sum of areas of all shapes
    print(paint.get_circles())  # Output: List of circles
    print(paint.get_squares())  # Output: List of squares
    print(paint.get_rectangles())  # Output: List of rectangles