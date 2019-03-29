import sys

def scores(a, b, c):
	return (a ** 2) + (b ** 2) + (c ** 2) + (7 * min(a, b, c)) 
def main():
	for line in sys.stdin:
		nums = line.strip().split()
		[a, b, c, d] = [int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])]
		if a < b and a < c:
			a = a + d
			print(scores(a, b, c))
		elif b < a and b < c:
			b = b + d
			print(scores(a, b, c))
		else:
			c = c + d
			print(scores(a, b, c))

if __name__ == '__main__':
	main()