"""
Create a class rectangle, jab bhi koi object banaeyga , on the spot we have
send two parameter into that
1.  x.area() -> should return me something
2   x.parameter() -> should return me something
3.  x.issquare()-> should return boolean 
"""


class Rectangle:
    def __init__(self, length: int, breadth: int) -> None:
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        return self.length * self.breadth

    def parameter(self) -> float:
        return 2 * (self.length + self.breadth)

    def issquare(self) -> bool:
        if self.length == self.breadth:
            return True
        return False


x = Rectangle(10, 20)
a = x.area()
print(a)
b = x.parameter()
print(b)
c = x.issquare()
print(c)
