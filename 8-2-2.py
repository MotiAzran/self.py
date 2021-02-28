def sort_prices(list_of_tuples):
	list_of_tuples.sort(key=lambda x: float(x[1]), reverse=True)
	return list_of_tuples
