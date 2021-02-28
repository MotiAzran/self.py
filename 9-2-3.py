def who_is_missing(file_name):
	with open(file_name, 'r') as f:
		nums = sorted(map(int, f.read().split(',')))

	for i, n in zip(range(1, nums[-1]), nums):
		if i != n:
			with open('found.txt', 'w') as f:
				f.write(str(i))

			return i
