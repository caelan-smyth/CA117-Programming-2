import sys

def main():
	longest = 0
	lines = []
	for line in sys.stdin:
		line = line.strip()
		lines.append(line)
		if len(line) > longest:
			longest = len(line)

	i = 0
	while i < len(lines):
		print("{:^{}s}".format(lines[i], longest))
		i += 1

if __name__ == '__main__':
	main()