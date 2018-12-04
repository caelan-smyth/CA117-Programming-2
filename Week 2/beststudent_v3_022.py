import sys

def best(filename):
	f = open(filename, "r")
	bestmark = 0
	best = ""
	for line in f:
		students = line.split()
		try:
			mark = int(students[0])
			name = " ".join(students[1:])
			if mark > bestmark:
				bestmark = mark
				best = name
		except(ValueError):
			print("Invalid mark {} encountered. Skipping.".format(students[0]))

	print("Best student: {}".format(best))
	print("Best mark: {}".format(bestmark))
	f.close()

def main():
	best(sys.argv[1])

if __name__ == '__main__':
	main()