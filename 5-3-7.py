def choclate_maker(small, big, x):
	if small + (big * 5) < x:
		return False

	if x == big * 5:
		return True
	elif x > big * 5:
		x = x - big * 5
		return x <= small
	else:
		big_n = int((big * 5) / x)
		x = x - big_n * 5
		return x <= small

