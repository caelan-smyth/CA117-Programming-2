import sys

def longest(s):
	caps = []
	i = 0

	while True:
		while i < len(s) and not s[i].isupper():
			i += 1
		if i >= len(s):
			return max(caps, default="", key=len)

		capstring = s[i]

		i += 1
		while i < len(s) and s[i].isupper():
			capstring += s[i]
			i += 1

		caps.append(capstring)

def main():
	for line in sys.stdin:
		print(longest(line.strip()))

if __name__ == '__main__':
	main()