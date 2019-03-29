import sys

def best(filename):
	try:
		f = open(filename, "r")
		bestmark = 0
		best = ""
		for line in f:
			students = line.split()
			mark = int(students[0])
			name = " ".join(students[1:])
			if mark > bestmark:
				bestmark = mark
				best = name

		print("Best student: {}".format(best))
		print("Best mark: {}".format(bestmark))
		f.close()

	except(ValueError):
		print("Invalid mark {} encountered. Exiting.".format(students[0]))

def main():
	s = sys.argv[1]
	best(s)

if __name__ == '__main__':
	main()