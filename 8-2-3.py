def mult_tuple(tuple1, tuple2):
	result = []
	for item1 in tuple1:
		for item2 in tuple2:
			result.append((item1, item2))
			result.append((item2, item1))

	return tuple(result)
