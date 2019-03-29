class Queue(object):

	def __init__(self):
		self.l = []

	def enqueue(self, e):
		self.l.append(e)

	def dequeue(self):
		return self.l.pop(0)

	def first(self):
		return self.l[0]

	def is_empty(self):
		return not self.l

	def __len__(self):
		return len(self.l)