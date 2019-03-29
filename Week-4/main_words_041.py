import sys
import string

def build_dict():
	d = {}
	for line in sys.stdin:
		words = line.lower().strip().split()
		for word in words:
			word = word.strip(string.punctuation)
			if len(word) > 3 and word not in d:
				d[word] = 1
			elif len(word) > 3:
				d[word] += 1
	frequency = sorted([k for k in d if 3 <= d[k]])

	wordwidth = len(max(frequency, key=len))
	numberwidth = len(str(max(d.values())))

	for w in frequency:
		print("{:>{:d}s} : {:>{:d}d}".format(w, wordwidth, d[w], numberwidth))

def main():
	d = build_dict()
	return d	

if __name__ == '__main__':
	main()