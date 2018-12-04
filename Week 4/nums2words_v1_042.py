import sys

def main():
	nums = {
	0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten"
	}
	for line in sys.stdin:
		lines = line.strip().split()
		for (i, n) in enumerate(lines, 1):
			if i == len(lines):
				print(nums[int(n)])
			else:
				print(nums[int(n)] + " ", end="")

if __name__ == '__main__':
	main()