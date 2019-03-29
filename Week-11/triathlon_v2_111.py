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

class Triathlon(Triathlete):

	def __init__(self):
		self.tri = {}

	def add(self, athlete):
		self.tri[athlete.tid] = athlete

	def remove(self, athlete):
		self.tri[athlete] = None

	def lookup(self, athlete):
		return self.tri[athlete]

	def __str__(self):
		strings = []
		for athlete in self.tri:
			strings.append([self.tri[athlete].name, self.tri[athlete].tid])

		form = []
		for string in sorted(strings):
			form.append("Name: {}".format(string[0]))
			form.append("ID: {}".format(string[1]))
		return "\n".join(form)

	def sorter(self):
		time = []
		for k in self.tri:
			time.append([self.tri[k].total_time(), self.tri[k].tid])
		return time

	def best(self):
		return self.tri[min(self.sorter())[1]]

	def worst(self):
		return self.tri[max(self.sorter())[1]]