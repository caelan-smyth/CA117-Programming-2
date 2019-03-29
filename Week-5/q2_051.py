import sys

def matches(w, s):
	return [c for c in w if c in s] == s

def main():
	lemons = list("evil")
	
	words = [line.strip() for line in sys.stdin]

	evil = [w for w in words if matches(w.lower(), lemons)]

	for w in evil:
		print(w)

if __name__ == '__main__':
	main()