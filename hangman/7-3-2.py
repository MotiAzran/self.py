def check_win(secret_word, old_letters_guessed):
    return all([c in old_letters_guessed for c in secret_word])
