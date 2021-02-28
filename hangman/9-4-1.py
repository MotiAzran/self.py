def choose_word(file_path, index):
	with open(file_path, 'r') as f:
		words = f.read().split(' ')

	return len(set(words)), words[(index - 1) % len(words)]
