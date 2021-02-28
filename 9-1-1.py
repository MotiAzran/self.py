def are_files_equal(file1, file2):
	with open(file1, 'rb') as f1:
		with open(file2, 'rb') as f2:
			return f1.read() == f2.read()
