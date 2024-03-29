# using the internal methods (len, iter, str) is the best choice
from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self): # repr就是通过__repr__这个特殊方法来得到一个对象的字符串表示形式的
        return "Vector(%r,%r)"%(self.x, self.y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self)) #  return bool(self.x or self.y) 更高效
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)