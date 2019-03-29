class Weight(object):
	OUNCES_PER_POUND = 16

	def __init__(self, pounds=0, ounces=0):
		self.pounds = pounds
		self.ounces = ounces

	def from_ounces(n):
		pounds = n // Weight.OUNCES_PER_POUND
		ounces = n % Weight.OUNCES_PER_POUND
		return Weight(pounds, ounces)

	def to_ounces(self):
		return self.pounds*16 + self.ounces

	def __add__(self, other):
		return Weight.from_ounces(self.to_ounces() + other.to_ounces())

	def __str__(self):
		return "{} pound(s) and {} ounce(s)".format(self.pounds, self.ounces)

	def __iadd__(self, other):
		z = self + other
		self.pounds, self.ounces = z.pounds, z.ounces
		return self

	def __mul__(self, n):
		return Weight.from_ounces(self.to_ounces() * n)

	def __eq__(self, other):
		return self.to_ounces() == other.to_ounces()

	def __ne__(self, other):
		return self.to_ounces() != other.to_ounces()

	def __lt__(self, other):
		return self.to_ounces() < other.to_ounces()

	def __le__(self, other):
		return self.to_ounces() <= other.to_ounces()

	def __gt__(self, other):
		return self.to_ounces() > other.to_ounces()

	def __ge__(self, other):
		return self.to_ounces() >= other.to_ounces()