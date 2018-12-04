import sys

def plural(s):
	es_endings = ["ch", "sh", "x", "s", "z", "o"]
	vowels = ["a", "e", "i", "o", "u"]
	f = "ves"
	if s[-2:] in es_endings or s[-1] in es_endings:
		s = s + "es"
	elif s[-1] == "y" and s[-2] in vowels:
		s = s[:-1] + "ies"
	elif s[-2:] == "fe":
		s = s[:-2] + f
	elif s[-1] == "f":
		s = s[:-1] + f
	else:
		s = s + "s"
	return s

def main():
	for line in sys.stdin:
		print(plural(line.split()))


if __name__ == '__main__':
	main()