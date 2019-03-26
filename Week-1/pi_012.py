import sys

from math import pi

def form(n):
	return "{:.{:d}f}".format(pi, n)

def main():
	print(form(int(sys.argv[1])))

if __name__ == '__main__':
	main()