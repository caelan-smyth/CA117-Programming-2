def maximum(a):
	if len(a) == 1:
		return a[0]

	if a[0] >= maximum(a[1:]):
		return a[0]
	else:
		return maximum(a[1:])