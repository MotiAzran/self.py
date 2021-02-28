def inverse_dict(my_dict):
	new_dict = dict()	
	for k, v in my_dict.items():
		new_dict[v] = sorted(new_dict.get(v, []) + [k])

	return new_dict
