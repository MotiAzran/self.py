def numbers_letters_count(my_str):
	digits_count = 0
	non_digits_count = 0
	for c in my_str:
		if c.isdigit():
			digits_count += 1
		else:
			non_digits_count += 1

	return [digits_count, non_digits_count]