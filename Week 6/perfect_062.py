import sys

def sumFac(n):
	factors = [i for i in range(1, (n//2) + 1) if not n % i]
	total = sum(factors)
	return total

def isPerfect(n):
	return n == sumFac(n)

def main():
	for line in sys.stdin:
		print(isPerfect(int(line.strip())))

if __name__ == '__main__':
	main()