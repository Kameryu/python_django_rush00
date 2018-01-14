from django.conf import settings
import os

class SavedData:

	def __init__(self):
		try:
			self.dlst = os.listdir("moviemon/saved_game")
		except:
			os.mkdir("moviemon/saved_game")
			self.dlst = list()
		self.pos = 0
		self.last = 0

	def get_game_list(self):
		my_list = self.dlst
		ret = dict()
		i = 0
		while i < len(my_list):
			my_split = my_list[i].split('.')[0].split('_')
			ret[my_split[0]] = my_split[1] + '/' + my_split[2]
			i += 1
		return (ret)

	def set_load(self, game):
		if self.pos == 0 or self.pos > len(self.dlst) + 1:
			return (0)
		self.last = self.pos
		game.load(self.dlst[self.last - 1])
