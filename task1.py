class Rectangle:
    """Rectangle class with getters and setters"""
    def __init__(self, width = 1.0, length = 1.0) :
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width):
        """Method which set width"""
        if not isinstance(width, float):
            raise TypeError("Wrong input type!")
        if not 0.0 < width < 20.0:
            raise ValueError("Wrong input value!")
        self.__width = width

    @length.setter
    def length(self, length):
        """Method which set length"""
        if not isinstance(length, float):
            raise TypeError("Wrong input type!")
        if not 0.0 < length < 20.0:
            raise ValueError("Wrong input value!")
        self.__length = length

    def area(self) :
        return self.width * self.length
    def perimeter(self) :
        return (self.width + self.length) * 2

rectangle1 = Rectangle()
rectangle1.width = 3.2
rectangle1.length = 2.8
print("Area: ", rectangle1.area())
print("Perimetr: ", rectangle1.perimeter())
rectangle2 = Rectangle(3.2, 2.8)
print("Area: ", rectangle2.area())
print("Perimetr: ", rectangle2.perimeter())
