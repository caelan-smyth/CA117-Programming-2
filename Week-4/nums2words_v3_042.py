import sys

def translate(file):
	trans = {}
	with open(file, "r") as f:
		for line in f:
			english, translation = line.strip().split()
			trans[english] = translation
	return trans

def main():
	trans = translate(sys.argv[1])
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
				print(trans[nums[int(n)]])
			else:
				print(trans[nums[int(n)]] + " ", end="")
			
if __name__ == '__main__':
	main()