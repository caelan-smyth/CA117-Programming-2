class PQ(object):

	def __init__(self):
		self.d = {}
		self.n = 0

	def switch(self, n, m):
		self.d[n], self.d[m] = self.d[m], self.d[n]

	def is_empty(self):
		return not self.d

	def size(self):
		return len(self.d)

	def swim(self, v):
		while v > 1 and self.d[v] > self.d[v // 2]:
			self.switch(v, v//2)
			v = v//2

	def sink(self, v):
		while v * 2 <= self.n:
			child = v * 2
			try:
				biggest_child = max([child, child + 1], key=self.d.__getitem__)
			except KeyError:
				biggest_child = child

			if self.d[v] >= self.d[biggest_child]:
				break

			self.switch(v, biggest_child)
			v = biggest_child

	def insert(self, v):
		self.n += 1
		self.d[self.n] = int(v)
		self.swim(self.n)

	def getMax(self):
		return self.d[1]

	def delMax(self):
		root = self.d[1]

		self.switch(1, self.n)
		del(self.d[self.n])
		self.n -= 1

		self.sink(1)
		return root