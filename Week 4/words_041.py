import sys
import string

def build_dict():
	a = []
	d = {}
	for line in sys.stdin:
		words = line.strip().casefold().split()
		for word in words:
			word = word.strip(string.punctuation)
			if word == "":
				continue
			if not word in d:
				d[word] = 1
				a.append(word)
			else:
				d[word] += 1
	a = sorted(a)
	for word in a:
		print("{} : {}".format(word, d[word]))

def main():
	build_dict()

if __name__ == '__main__':
	main()