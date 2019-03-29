import sys

def poker(n):
	total = 0
	total0 = 0
	total1 = 0
	total2 = 0
	total3 = 0
	total4 = 0
	total5 = 0
	total6 = 0
	total7 = 0
	total8 = 0
	total9 = 0
	if int(n[-1]) == 0:
		total0 += 1
		total += 1
	elif int(n[-1]) == 1:
		total1 += 1
		total += 1
	elif int(n[-1]) == 2:
		total2 += 1
		total += 1
	elif int(n[-1]) == 3:
		total3 += 1
		total += 1
	elif int(n[-1]) == 4:
		total4 += 1
		total += 1
	elif int(n[-1]) == 5:
		total5 += 1
		total += 1
	elif int(n[-1]) == 6:
		total6 += 1
		total += 1
	elif int(n[-1]) == 7:
		total7 += 1
		total += 1
	elif int(n[-1]) == 8:
		total8 += 1
		total += 1
	elif int(n[-1]) == 9:
		total9 += 1
		total += 1

def main():
	for line in sys.stdin:
		poker(line)

	


if __name__ == '__main__':
	main()