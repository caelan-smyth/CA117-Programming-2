import sys

import calendar

def birthday(first, second, third):
	day = calendar.weekday(first, second, third)
	if day == 0:
		return "You were born on a Monday and Monday's child is fair of face."
	elif day == 1:
		return "You were born on a Tuesday and Tuesday's child is full of grace."
	elif day == 2:
		return "You were born on a Wednesday and Wednesday's child is full of woe."
	elif day == 3:
		return "You were born on a Thursday and Thursday's child has far to go."
	elif day == 4:
		return "You were born on a Friday and Friday's child is loving and giving."
	elif day == 5:
		return "You were born on a Saturday and Saturday's child is loving and giving."
	else:
		return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."


def main():
		s1 = int(sys.argv[1])
		s2 = int(sys.argv[2])
		s3 = int(sys.argv[3])
		print(birthday(s3, s2, s1))

if __name__ == '__main__':
	main()