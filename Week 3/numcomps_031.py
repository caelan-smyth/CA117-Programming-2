import sys

def replace(n):
	if not n % 3:
		return "X"
	else:
		return n

def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2, n):
			if not n % i:
				return False
		return True

def mult3(nums):
	return [n for n in nums if not n % 3]

def sqmult3(nums):
	return [n * n for n in nums if not n % 3]

def mult4by2(nums):
	return [n * 2 for n in nums if not n % 4]

def mult3or4(nums):
	return [n for n in nums if not n % 3 or not n % 4]

def mult3and4(nums):
	return [n for n in nums if not n % 3 and not n % 4]

def main():
	l = [i for i in range(1, int(sys.argv[1]) + 1)]
	print("Multiples of 3: {}".format(mult3(l)))
	print("Multiples of 3 squared: {}".format(sqmult3(l)))
	print("Multiples of 4 doubled: {}".format(mult4by2(l)))
	print("Multiples of 3 or 4: {}".format(mult3or4(l)))
	print("Multiples of 3 and 4: {}".format(mult3and4(l)))
	print("Multiples of 3 replaced: {}".format([replace(n) for n in l]))
	print("Primes: {}".format([n for n in l if is_prime(n)]))

if __name__ == '__main__':
	main()