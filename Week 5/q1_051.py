import sys
def main():
	s = sys.argv[1]

	new_s = list(s)

	for i in range(1, len(s), 2):
		new_s[i-1], new_s[i] = new_s[i], new_s[i-1]
	print("".join(new_s))

if __name__ == '__main__':
	main()