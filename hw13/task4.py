class Player:
	def add_to_playlist(self):
		print('add to playlist')

	def play(self):
		print('play')

	def delete_from_playlist(self):
		print('delete from playlist')

	def shuffle(self):
		print('shuffle')


class AudioPlayer(Player):
	pass


class VideoPlayer(Player):
	pass


a, v = AudioPlayer(), VideoPlayer()

a.add_to_playlist()
a.play()
a.delete_from_playlist()
a.shuffle()

v.add_to_playlist()
v.play()
v.delete_from_playlist()
v.shuffle()