def handle_sort(path):
	with open(path, 'r') as f:
		print(sorted(list(set(f.read().split(' ')))))


def handle_reverse(path):
	f = open(path, 'r')
	for line in f:
		print(line[-1::-1])

	f.close()


def handle_last(path, n):
	with open(path, 'r') as f:
		for line in f.readlines()[-n:]:
			print(line)


def main():
	path = input('Please enter file path: ')
	action = input('Enter an action (sort, rev or last): ')

	if action == 'sort':
		handle_sort(path)
	elif action == 'rev':
		handle_reverse(path)
	elif action == 'last':
		n = int(input('Enter number of lines to print: '))
		handle_last(path, n)


if __name__ == '__main__':
	main()
