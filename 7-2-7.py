def arrow(my_char, max_length):
	result = ''
	for i in range(1, max_length):
		result += (my_char * i) + '\n'

	result += (my_char * max_length) + '\n'

	for i in range(max_length - 1, 0, -1):
		result += (my_char * i) + '\n'

	return result
