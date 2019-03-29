import sys

class Stack(object):

	def __init__(self):
		self.l = []

	def push(self, e):
		self.l.append(e)

	def pop(self):
		return self.l.pop()

class Queue(object):

	def __init__(self):
		self.l = []

	def enqueue(self, e):
		self.l.append(e)

	def dequeue(self):
		self.l.pop(0)

	def __len__(self):
		return len(self.l)

def isflt(n):
	try:
		float(n)
		return True
	except ValueError:
		return False

def calculator(line):
	s = Stack()
	q = Queue()

	def plus(a, b):
		return a + b

	def minus(a, b):
		return a - b

	def mult(a, b):
		return a * b

	def div(a, b):
		return a / b

	def sqrt(a):
		return a ** (1/2)

	def neg(a):
		return -a

	binops = {
	"+", plus
	"-", minus
	"*", mult
	"/", div
	}

	uniops = {

	}

	lines = line.split()
	i = 0
	while i < len(lines) and isflt(lines[i]):
		s.push(float(lines[i]))
		i += 1

	while i < len(lines):
		q.enqueue(lines[i])
		i += 1

	while len(q) > 0:
		op = q.dequeue()
		n1 = s.pop()

		if op in uniops:
			s.push(uniops[op](n1))
		
		else:
			n2 = s.pop()
			n3 = eval(str(n2) + binops[op] + str(n1))