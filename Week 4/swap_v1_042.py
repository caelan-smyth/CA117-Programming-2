import sys

def swap_keys_values(d):
	nd = {}
	for k, v in d.items():
		nd[v] = k
	return nd

def main():
	d = {"a": 4, "b": 7, "c": 10}
	print(swap_keys_values(d))

if __name__ == '__main__':
	main()