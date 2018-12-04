def reverse_list(a):
	if len(a) == 0:
		b = list()
		return b

	else:
		b = reverse_list(a[1:])
		b.append(a[0])
		return b