from math import sqrt

class Point(object):

	def __init__(self, x=0, y=0):
		self.xval = x
		self.yval = y

	def reflect(self):
		self.xval = self.xval * -1
		self.yval = self.yval * -1

	def distance(self, other):
		return sqrt(((other.xval - self.xval) ** 2) + ((other.yval - self.yval) ** 2))