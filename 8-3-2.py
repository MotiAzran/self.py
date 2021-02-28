import datetime

DATE_FORMAT = '%d.%m.%Y'
person_data = {'first_name': 'Mariah', 'last_name': 'Carey', 'birth_date': '27.03.1970', 'hobbies': ['Sing', 'Compose', 'Act']}


def print_menu():
	print('1. Print Mariah last name')
	print('2. Print Mariah birth month')
	print('3. Print number of Mariah\'s hobbies')
	print('4. Print one of Mariah\'s hobbies')
	print('5. Add Mariah Cooking hobby')
	print('6. Print Mariah birth date tuple')
	print('7. Print Mariah\'s age')
	print('8. Exit')


def main():
	while True:
		print_menu()
		choice = int(input('Please enter your choice: '))
		print()

		if choice == 1:
			print(person_data['last_name'])
		elif choice == 2:
			print(datetime.datetime.strptime(person_data['birth_date'], DATE_FORMAT).month)
		elif choice == 3:
			print(len(person_data['hobbies']))
		elif choice == 4:
			print(person_data['hobbies'][-1])
		elif choice == 5:
			person_data['hobbies'].append('Cooking')
		elif choice == 6:
			print(tuple(person_data['birth_date'].split('.')))
		elif choice == 7:
			birth_year = datetime.datetime.now().year - datetime.datetime.strptime(person_data['birth_date'], DATE_FORMAT).year
			person_data['age'] = birth_year
			print(birth_year)
		elif choice == 8:
			break

		print()


if __name__ == '__main__':
	main()