letter = input("Guess a letter: ")
if len(letter) > 1 and not letter.isalpha():
	print("E3")
elif len(letter) > 1:
	print("E1")
elif not letter.isalpha():
	print("E2")
elif len(letter) == 1 and letter.isalpha():
	print(letter.lower())
