def print_menu():
	print()
	print('1. Print groceries list')
	print('2. Print number of groceries')
	print('3. Check if grocery is in the list')
	print('4. Check how many times grocery appers in the list')
	print('5. Delete grocery')
	print('6. Add grocery')
	print('7. Print invalid groceries')
	print('8. Remove duplicates')
	print('9. Exit')


def print_groceries(groceries):
	for item in groceries:
		print(item)


def check_if_in_groceries(groceries):
	item = input('Enter grocery to check: ')
	print(item in groceries)


def check_item_count(groceries):
	item = input('Enter grocery to count: ')
	print(groceries.count(item))


def delete_item(groceries):
	item = input('Enter grocery to delete: ')
	if item in groceries:
		groceries.remove(item)

	return groceries


def add_grocery(groceries):
	item = input('Enter grocery to add: ')
	groceries.append(item)

	return groceries


def print_invalid_groceries(groceries):
	for item in groceries:
		if len(item) < 3 or not item.isalpha():
			print(item)


def remove_duplicates(groceries):
	new_groceries = []
	for i, item in enumerate(groceries):
		if item not in groceries[:i]:
			new_groceries.append(item)

	return new_groceries


def main():
	groceries = input('Enter groceries: ').split(',')
	while True:
		print_menu()
		choice = int(input('Enter your choice: '))
		print()
		if choice == 1:
			print_groceries(groceries)
		elif choice == 2:
			print(len(groceries))
		elif choice == 3:
			check_if_in_groceries(groceries)
		elif choice == 4:
			check_item_count(groceries)
		elif choice == 5:
			groceries = delete_item(groceries)
		elif choice == 6:
			groceries = add_grocery(groceries)
		elif choice == 7:
			print_invalid_groceries(groceries)
		elif choice == 8:
			groceries = remove_duplicates(groceries)
		elif choice == 9:
			break

if __name__ == '__main__':
	main()