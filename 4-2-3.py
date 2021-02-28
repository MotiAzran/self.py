temperature = input("Insert the temperature you would like to convert: ")
if temperature[-1].upper() == 'F':
	print(str(((5 * float(temperature[:-1])) - 160) / 9) + 'C')
elif temperature[-1].upper() == 'C':
	print(str(((9 * float(temperature[:-1])) + 160) / 5) + 'F')