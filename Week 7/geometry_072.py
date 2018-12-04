from math import sqrt

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, other):
		return sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

	def __str__(self):
		return ("({:.1f}, {:.1f})".format(self.x, self.y))

class Segment(object):

	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def midpoint(self):
		x = (self.p1.x + self.p2.x) / 2
		y = (self.p1.y + self.p2.y) / 2
		return Point(x, y)

	def length(self):
		return self.p1.distance(self.p2)

class Circle(object):

	def __init__(self, c, r):
		self.radius = r
		self.centre = c

	def overlaps(self, other):
		return self.centre.distance(other.centre) < self.radius + other.radius