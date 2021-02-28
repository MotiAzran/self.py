msg = input("Please enter a string: ")
print(msg[:len(msg) // 2].lower() + msg[len(msg) // 2:].upper())