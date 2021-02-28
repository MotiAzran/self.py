def longest(my_list):
	my_list.sort(key=lambda x: len(x))
	return my_list[-1]