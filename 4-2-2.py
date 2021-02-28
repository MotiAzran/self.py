msg = input("Enter a word: ")
if msg.replace(' ', '').lower() == msg.replace(' ', '').lower()[-1::-1]:
	print('OK')
else:
	print('NOT')