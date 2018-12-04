import sys

def swap_unique_keys_values(d):
	nd = {}
	for k, v in d.items():
		if not v in nd:
			nd[v] = k
		else:
			del nd[v]
	return nd

def main():
	d = {"a": 4, "b": 7, "c": 10}
	print(swap_unique_keys_values(d))

if __name__ == '__main__':
	main()