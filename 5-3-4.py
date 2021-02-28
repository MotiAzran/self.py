def last_early(my_str):
	return my_str[:-1].lower().find(my_str[-1].lower()) != -1
