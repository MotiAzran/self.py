def my_mp4_playlist(file_path, new_song):
	with open(file_path, 'r') as f:
		songs = [song.split(';') for song in f.readlines()]

	while len(songs) < 3:
		songs.append(['', '', '', ''])

	songs[2][0] = new_song

	new_data = ''.join([';'.join(song) for song in songs])
	with open(file_path, 'w') as f:
		f.write(new_data)

	return new_data
