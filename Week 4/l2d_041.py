import sys

def l2d(file):
	f = file.read().split()
	
	keys = f[:len(f)//2]
	values = f[len(f)//2:]

	#print(keys)
	#print(values)
	d = {}
	i = 0
	while i < len(keys):
		d[keys[i]] = values[i]
		i += 1
	return d

		

def main():
	l2d(sys.stdin)

if __name__ == '__main__':
	main()