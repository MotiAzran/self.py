def count_chars(my_str):
	count = dict()
	for c in my_str:
		if not c.isalpha():
			continue

		if c in count.keys():
			count[c] += 1
		else:
			count[c] = 1

	return count
