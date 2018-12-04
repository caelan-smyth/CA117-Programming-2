class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.times = {}

	def add_time(self, race, time):
		self.times[race] = time

	def get_time(self, race):
		return self.times[race]

	def total_time(self):
		return sum([t for t in self.times.values()])

	def __eq__(self, other):
		return self.total_time() == other.total_time()

	def __gt__(self, other):
		return self.total_time() > other.total_time()

	def __lt__(self, other):
		return self.total_time() < other.total_time() 

	def __str__(self):
		return ("Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, self.total_time()))