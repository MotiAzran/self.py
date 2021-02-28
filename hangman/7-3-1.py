def show_hidden_word(secret_word, old_letters_guessed):
	# result = ' '.join([c if c in old_letters_guessed else '_' for c in secret_word])
	result = ''
	for c in secret_word:
		if c in old_letters_guessed:
			result += (c + ' ')
		else:
			result += '_ '

	return result
