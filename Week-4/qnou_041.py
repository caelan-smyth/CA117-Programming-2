import sys

def qnou(s):
	return "q" in s and s.count("q") > s.count("qu")

def main():
	a = []
	for line in sys.stdin:
		a.append(line.strip())

	print("Words with q but no u: {}".format([w for w in a if qnou(w.casefold())]))

if __name__ == '__main__':
	main()