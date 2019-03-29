import sys

def best(filename):
	try:
		f = open(filename, "r")
		bestmark = 0
		best = ""
		for line in f:
			students = line.split()
			try:
				mark = int(students[0])
				name = " ".join(students[1:])
				if mark == bestmark:
					best = best + ", " + name
				elif mark > bestmark:
					bestmark = mark
					best = name
			except(ValueError):
				print("Invalid mark {} encountered. Skipping.".format(students[0]))
			
		print("Best student(s): {}".format(best))
		print("Best mark: {}".format(bestmark))

		f.close()

	except(FileNotFoundError):
		print("The file {} could not be opened.".format(filename))

def main():
	best(sys.argv[1])

if __name__ == '__main__':
	main()