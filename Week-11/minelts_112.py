import sys

class Min_Queue(object):

	def __init__(self):
		self.d = {}
		self.p = 0

	def swim(self, pos):
		while pos > 1 and self.d[pos] < self.d[pos//2]:
			self.d[pos], self.d[pos//2] = self.d[pos//2], self.d[pos]
			pos = pos//2

	def sink(self, pos):
		while pos * 2 <= self.p:
			child = pos * 2
			try:
				better_child = min([child, child + 1], key = self.d.__getitem__)
			except KeyError:
				better_child = child

			if self.d[pos] < self.d[better_child]:
				break

			self.d[pos], self.d[better_child] = self.d[better_child], self.d[pos]
			pos = better_child


	def insert(self, number):
		self.p += 1
		self.d[self.p] = number
		self.swim(self.p)

	def check(self, number):
		if max(self.d.values()) > number:

			i = 1
			while self.d[i] != max(self.d.values()):
				i += 1

			self.d[i] = number
			self.swim(i) 

	def delmin(self):
		root = self.d[1]
		self.d[1], self.d[len(self.d)] = self.d[len(self.d)], self.d[1]
		
		del(self.d[self.p])
		self.p -= 1
		
		self.sink(1)
		return root 


def main():

	num_of_small = int(sys.argv[1])
	min_numbers = Min_Queue()

	for line in sys.stdin.readlines():
		number = int(line.strip())

		if len(min_numbers.d) < num_of_small:
			min_numbers.insert(number)

		else:
			min_numbers.check(number)
	
	ordered = []
	for i in range(0, len(min_numbers.d)):
		ordered.append(min_numbers.delmin())
		i += 1	

	for i in range(0, len(ordered)):
		print(ordered[len(ordered) - 1 - i])
		i += 1

if __name__ == '__main__':
	main()