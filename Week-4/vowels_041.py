import sys

vowels = "aeiou"
d = {
"a": 0,
"e": 0,
"i": 0,
"o": 0,
"u": 0
}

def sort(t):
	return t[1]

def vowelcount(s):
	for vowel in vowels:
		d[vowel] += s.count(vowel)
	return d

def main():
	for line in sys.stdin:
		line = line.strip().casefold()
		d = vowelcount(line)
	numwidth = len(str(max(d.values())))
	for (k, v) in sorted(d.items(), key=sort, reverse=True):
		print("{:s} : {:>{}d}".format(k, v, numwidth))

if __name__ == '__main__':
	main()