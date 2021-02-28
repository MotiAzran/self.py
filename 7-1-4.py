def squared_numbers(start, stop):
	i = start
	squared_numbers = []
	while i <= stop:
		squared_numbers.append(i**2)
		i += 1

	return squared_numbers