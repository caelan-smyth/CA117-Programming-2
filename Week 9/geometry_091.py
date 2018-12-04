class Point(object):

   def __init__(self, x, y):
      self.x = int(x)
      self.y = int(y)

   def distance(self, other):
      xt = self.x - other.x
      yt = self.y - other.y

      return float(((xt ** 2) + (yt ** 2)) ** (1/2))

class Shape(object):

   def __init__(self, lisp):
      self.points = lisp

   def sides(self):
      length = []

      for i in range(0, len(self.points) - 1):
         length.append(self.points[i].distance(self.points[i + 1]))
         i += 1

      length.append(self.points[-1].distance(self.points[0]))
      return length

   def perimeter(self):
      return sum(self.sides())


class Triangle(Shape):

   def area(self):
      sides = self.sides()
      s = sum(sides) / 2

      return (s * (s - sides[0]) * (s - sides[1]) * (s - sides[2])) ** (1/2)


class Square(Shape):

   def area(self):
      return (self.sides()[0]) ** 2