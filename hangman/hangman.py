MAX_TRIES = 6
HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/"""

HANGMAN_PHOTOS = [
    """    x-------x\n""",
    """    x-------x
    |
    |
    |
    |
    |\n""",
    """    x-------x
    |       |
    |       0
    |
    |
    |\n""",
    """    x-------x
    |       |
    |       0
    |       |
    |
    |\n""",
    """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |\n""",
    """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |\n""",
    """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |\n"""
]


def choose_word(file_path, index):
    """Choose the word in the index place from file
    :param file_path: path to file
    :param index: word index
    :type file_path: str
    :type index: int
    :return: The word at the index place of the file
    :rtype: str
    """
    with open(file_path, 'r') as f:
        words = f.read().split(' ')

    return words[index - 1]


def check_win(secret_word, old_letters_guessed):
    """Check if all the letters in secret_word were guessed
    :param secret_word: the secret word to guess
    :param old_letters_guessed: list of guessed letters
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if all secred_word guessed, else False
    :rtype: bool
    """
    return all([c in old_letters_guessed for c in secret_word])


def show_hidden_word(secret_word, old_letters_guessed):
    """Get the word with only the guessed words shown
    :param secret_word: The secret word to guess
    :param old_letters_guessed: list of guessed letters
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The secret word with only the guessed letters
    :rtype: str
    """
    return ' '.join([c if c in old_letters_guessed else '_' for c in secret_word])


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check the input is a single letter that didn't entered before
    :param letter_guessed: The input letter
    :param old_letters_guessed: list of guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, else False
    :rtype: bool
    """
    return len(letter_guessed) == 1 and letter_guessed.isalpha() and letter_guessed.lower() not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Print error on invalid input,
    on valid input add it the guessed letters list
    :param letter_guessed: the input letter
    :param old_letters_guessed: list of guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True if the input is valid, else False
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print(' -> '.join(map(lambda x: x.lower(), old_letters_guessed)))
        return False

    old_letters_guessed.append(letter_guessed)
    return True


def print_hangman(num_of_tries):
    """Print current hangman stage
    :param num_of_tries: current number of failed tries
    :type num_of_tries: int
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def print_opening():
    """Print game openning message"""
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)


def choose_secret_word():
    """Choose game secret word"""
    file_path = input('Please enter words file path: ')
    word_index = int(input('Please enter word index: '))
    return choose_word(file_path, word_index)


def get_letter(letter_guessed):
    """Get input letter"""
    letter = input('Guess a letter: ')
    while not try_update_letter_guessed(letter, letter_guessed):
        letter = input('Guess a letter: ')

    return letter


def main():
    print_opening()

    secret_word = choose_secret_word()
    letter_guessed = []
    num_of_tries = 0

    print('Let\'s start!')
    print()

    while not check_win(secret_word, letter_guessed):
        print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, letter_guessed))
        letter = get_letter(letter_guessed)

        if letter not in secret_word:
            print(':(')
            num_of_tries += 1
            if num_of_tries == MAX_TRIES:
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, letter_guessed))
                print('LOSE')
                return

    print(show_hidden_word(secret_word, letter_guessed))
    print('WIN')


if __name__ == '__main__':
    main()
