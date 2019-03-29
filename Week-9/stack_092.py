class Stack(object):

	def __init__(self):
		self.l = []

	def push(self, e):
		self.l.append(e)

	def pop(self):
		return self.l.pop()

	def top(self):
		return self.l[-1]

	def is_empty(self):
		if not self.l:
			return True
		else:
			return False

	def __len__(self):
		return len(self.l)

def main():
   stack = Stack()
   stack.push("A")
   stack.push("B")
   stack.push("C")
   l = stack.pop()
   m = stack.pop()
   n = stack.pop()
   stack.push(n)
   stack.push(m)
   stack.push(m)
   m = stack.pop()
   print(stack)

if __name__ == '__main__':
   main()