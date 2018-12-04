import sys

def sorter(t):
	return(t[-1])

def main():
	d = {}
	
	nums = [int(line.strip()) for line in sys.stdin]

	N = len(nums)

	total = sum(nums)

	for n in nums:
		if n in d:
			d[n] += 1
		else:
			d[n] = 1

	mean = total / N

	mode_tuple = max(d.items(), key=sorter)
	mode = mode_tuple[0]

	snums = sorted(nums)
	if N % 2:
		median = snums[N//2]
	else:
		median = (snums[N//2 - 1] + snums[N//2]) / 2

	print("Mean: {:.1f}".format(mean))
	print("Mode: {:.1f}".format(mode))
	print("Median: {:.1f}".format(median))

if __name__ == '__main__':
	main()