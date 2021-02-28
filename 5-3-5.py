def distance(num1, num2, num3):
	return (abs(num1 - num2) == 1 or abs(num1 - num3) == 1) and (abs(num1 - num2) > 1 or abs(num1 - num3) > 1)
