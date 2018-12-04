import sys

class Stack(object):

	def __init__(self):
		self.l = []

	def push(self, e):
		self.l.append(e)

	def pop(self):
		return self.l.pop()

	def __len__(self):
		return len(self.l)

def matcher(line):
	bra = Stack()
	cur = Stack()
	squ = Stack()
	result = True

	dic = {
		'(' : bra,
		')' : bra,
		'{' : cur,
		'}' : cur,
		'[' : squ,
		']' : squ,
	}

	opened = ['(', '{', '[']

	for i in range(0, len(line)):
		if line[i] in opened:
			dic[line[i]].push(line[i])
		else:
			try:
				result = dic[line[i]].pop()
			except IndexError:
				return False

		i += 1


	return not bool(len(bra) + len(cur) + len(squ))