def find_longest_song(songs):
	times = {song[0]: tuple([int(n) for n in song[2].split(':')]) for song in songs}

	max_min , max_sec = 0, 0
	for m, s in times.values():
		if m > max_min:
			max_min, max_sec = m, s
		elif m == max_min:
			if s > max_sec:
				max_min, max_sec = m, s

	return list(times.keys())[list(times.values()).index((max_min, max_sec))]


def find_common_artist(songs):
	artist_count = dict()
	for song in songs:
		artist = song[1]
		if artist in artist_count.keys():
			artist_count[artist] += 1
		else:
			artist_count[artist] = 1

	max_occ = max(artist_count.values())
	return list(artist_count.keys())[list(artist_count.values()).index(max_occ)]


def my_mp3_playlist(file_path):
	with open(file_path, 'r') as f:
		songs = [song.split(';')[:-1] for song in f.readlines()]

	longest_song = find_longest_song(songs)
	common_artist = find_common_artist(songs)

	return longest_song, len(songs), common_artist
