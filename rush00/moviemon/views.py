from django.shortcuts import render, redirect
from moviemon.moviemon_data import MovieMonData
from moviemon.saved_data import SavedData

data = SavedData()
game = MovieMonData()

# Create your views here.
def titlescreen(request):
	return render(request, "moviemon/titlescreen.html")

def worldmap(request, param = None):
	if bool(game.dic) is False:
		game.load_default_settings()

	if param == 'left':
		if game.dic['pos'][1] > game.dic['sizey'][0]:
			game.dic['pos'][1] -= 1
			game.is_moving()
	if param == 'right':
		if game.dic['pos'][1] < game.dic['sizey'][-1]:
			game.dic['pos'][1] += 1
			game.is_moving()
	if param == 'up':
		if game.dic['pos'][0] > game.dic['sizex'][0]:
			game.dic['pos'][0] -= 1
			game.is_moving()
	if param == 'down':
		if game.dic['pos'][0] < game.dic['sizex'][-1]:
			game.dic['pos'][0] += 1
			game.is_moving()

	return render(request, "moviemon/worldmap.html", game.dic)

def battle(request):
	return render(request, "moviemon/battle.html")

def moviedex(request):
	return render(request, "moviemon/moviedex.html")

def options(request):
	return render(request, "moviemon/options.html")

def save_game(request):
	#to_save(slot, game)
	return render(request, "moviemon/save_game.html")

def load_game(request, param = None):
	rend = dict()
	
	if param == 'up':
		if data.pos == 1 or data.pos == 0:
			data.pos = 3
		else:
			data.pos -= 1
	if param == 'down':
		if data.pos == 3 or data.pos == 0:
			data.pos = 1
		else:
			data.pos += 1

	rend['pos'] = data.pos
	slots = data.get_game_list();
	for key, value in slots:
		rend[key] = slots[key][value]

	return render(request, "moviemon/load_game.html", rend)
