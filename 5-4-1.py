def func(num1, num2):
	"""Calculate the sum of the numbers
	:param num1: First number
	:type num1: int
	:param num2: Second number
	:type num2: int
	:return: The sum of the numbers
	:rtype: int
	"""
	return num1 + num2


def main():
	print(func.__doc__)


if __name__ == '__main__':
	main()
