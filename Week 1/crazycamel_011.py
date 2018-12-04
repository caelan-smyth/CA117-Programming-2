import sys

def split(s):
	return s.split()

def main():
	for line in sys.stdin:
		cs = split(line.strip())
		a = ""
		for word in cs:
			a = a + word[0:-1] + word[-1].upper() + " "
		print(a.strip())


if __name__ == '__main__':
	main()