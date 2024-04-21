"""
Assignment: Contact Manager
Class: DEV 128
Date: 01/24/24
Author: Nick Johnson

Point class creates a single x,y coordinate pair

Rectangle class has an instance of Point class for the Top Left point
Rectangle class uses properties for getter and setter methods
Rectangle class can calculate area and perimeter as read-only properities

Both classes use private variables
Both classes have a translate function to change the Top-Left point of the Rectangle class
"""
import copy


class Point:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    @property  # read-only
    def x(self):
        return self.__x

    @property  # read-only
    def y(self):
        return self.__y

    def translate(self, dx: int, dy: int) -> None:
        self.__x += dx
        self.__y += dy


class Rectangle:
    DEFAULT_WIDTH: int = 1
    DEFAULT_HEIGHT: int = 1
    rectangle_count: int = 0

    def __init__(self, top_left: Point, width: int, height: int):
        self.__top_left = top_left

        if width <= 0:
            self.__width = Rectangle.DEFAULT_WIDTH
            print(
                "Width cannot be negative or zero. Setting it to the default value of 1"
            )
        else:
            self.__width = width

        if height <= 0:
            self.__height = Rectangle.DEFAULT_HEIGHT
            print(
                "Height cannot be negative or zero. Setting it to the default value of 1"
            )
        else:
            self.__height = height

        Rectangle.rectangle_count += 1

    @property
    def top_left(self):
        return self.__top_left

    @top_left.setter
    def top_left(self, top_left: Point):
        self.__top_left = top_left

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height <= 0:
            print("Height cannot be 0 or lower")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if width <= 0:
            print("Width cannot be 0 or lower")
        else:
            self.__width = width

    @property  # read-only
    def bottom_right(self) -> Point:
        # use copy module since "="" does obj reference; so we don't overwrite the top_left coordinates
        # I imagine this isn't the expected way to do this, what is?
        top_left = copy.copy(self.__top_left)
        top_left.translate(self.__width, self.__height)

        return Point(top_left.x, top_left.y)

    @property  # read-only
    def area(self) -> int:
        return self.__width * self.__height

    @property  # read-only
    def perimeter(self) -> int:
        return 2 * (self.__width + self.__height)

    def translate(self, dx: int, dy: int) -> Point:
        return self.top_left.translate(dx, dy)


# p = Point(1, 1)
# r = Rectangle(p, 1, 1)
# print(r.bottom_right.x, r.bottom_right.y)
# r.translate(1, 1)
# print(r.top_left.x, r.top_left.y)
# print(r.bottom_right.x, r.bottom_right.y)
