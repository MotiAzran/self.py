def copy_file_content(source, destination):
	with open(source, 'r') as src:
		with open(destination, 'w') as dst:
			dst.write(src.read())
