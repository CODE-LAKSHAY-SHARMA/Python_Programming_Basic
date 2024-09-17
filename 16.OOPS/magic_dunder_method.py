# magic /dunder methods
class Rectangle:
    def __init__(self, length: int, breadth: int) -> None:
        self.length = length
        self.breadth = breadth

    # basic give the backend what going on when X (addresss) got print
    def __str__(self) -> str:
        return f"Length = {self.length} Breadth ={self.breadth}"

    def area(self) -> float:
        return self.length * self.breadth

    def parameter(self) -> float:
        return 2 * (self.length + self.breadth)

    def issquare(self) -> bool:
        if self.length == self.breadth:
            return True
        return False


x = Rectangle(10, 20)
y = Rectangle(20, 30)
print(x)
print(y)

# my_list = [1, 3, 4, 535]
# print(my_list)   # why this printing the list wherease in above print X it give addrres
