class Element(object):

	def __init__(self, n, s1, s2, s3):
		self.number = n
		self.name = s1
		self.symbol = s2
		self.boiling_point = s3

	def print_details(self):
		print("Number: {:d}".format(self.number))
		print("Name: {:s}".format(self.name))
		print("Symbol: {:s}".format(self.symbol))
		print("Boiling point: {} K".format(self.boiling_point))
