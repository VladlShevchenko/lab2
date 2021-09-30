class Rectangle:
    def __init__(self, width = 1, length = 1) :
        self.__width = width
        self.__length = length

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def set_width(self, width):
        if(0.0 < width < 20.0): 
            self.__width = width
        else: 
            print("Wrong input!")

    @property
    def length(self):
        return self.__length

    @length.setter
    def set_length(self, length):
        if(0.0 <length < 20.0): 
            self.__length = length
        else: 
            print("Wrong input!")
    
    def area(self) :
        return self.__width * self.__length

    def perimeter(self) :
        return (self.__width + self.__length) * 2

rec1 = Rectangle()

result = rec1.perimeter()
print("Default values:")
print("Default length is:", rec1.length)
print("Default width is:", rec1.width)
print(result)

print("New values length = 3.2 and width = 2.8")
rec2 = Rectangle(3.2, 2.8)
print("Area: ", rec2.area())
print("Perimetr: ", rec2.perimeter())
