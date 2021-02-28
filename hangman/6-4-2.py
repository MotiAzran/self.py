def check_valid_input(letter_guessed, old_letters_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(' -> '.join(map(lambda x: x.lower(), old_letters_guessed)))
        return False

    old_letters_guessed.append(letter_guessed)
    return True
