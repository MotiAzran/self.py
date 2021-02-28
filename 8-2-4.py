def is_anagrams(str1, str2):
	if len(str1) != len(str2):
		return False

	for c in str1:
		if c not in str2:
			return False

	for c in str2:
		if c not in str1:
			return False

	return True


def sort_anagrams(list_of_strings):
	result = []
	for data in list_of_strings:
		if not any([data in l for l in result]):
			result.append([data2 for data2 in list_of_strings if is_anagrams(data, data2)])

	return result
