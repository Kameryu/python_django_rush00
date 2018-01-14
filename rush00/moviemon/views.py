from django.shortcuts import render, redirect
from moviemon.moviemon_data import MovieMonData
import random

game = MovieMonData()

# Create your views here.
def titlescreen(request):
    return render(request, "moviemon/titlescreen.html")

def worldmap(request, param = None):
    if bool(game.dic) is False:
        game.load_default_settings()
        print("initialisation")

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

def battle(request, moviemon_id = None, param = None):
    if param == 'catch':
        chance = 50.0 - (10.0 * float(game.dic['encounter'][1][2])) + (5.0 * float(len(game.dic['movies_in_pocket'])))
        chance = int(chance)
        print("chance =", chance)
        if chance < 1:
            chance = 1
        elif chance > 90:
            chance = 90
        print("chance correct =", chance)
        nb = (random.randint(1, 90))
        if chance >= nb:
            print("OUI Je tai attrape")
            game.dic['encounter'][0] = False
            game.dic['encounter'][2] = False
            game.dic['movies_in_pocket'].append(game.dic['encounter'][1])
            print("il fait en enlever ", len(game.dic['movies_to_catch']))
            print("count =", game.dic['movies_to_catch'].count(game.dic['movies_to_catch']))
        else:
            game.dic['encounter'][2] = True
        if game.dic['ball'] > 0:
            game.dic['ball'] -= 1
    return render(request, "moviemon/battle.html", game.dic)

def moviedex(request):
    return render(request, "moviemon/moviedex.html", game.dic)

def options(request):
    return render(request, "moviemon/options.html")

def save_game(request):
    return render(request, "moviemon/save_game.html")

def load_game(request, param = None):
    rend = dict({'slota':'Free', 'slotb':'Free', 'slotc':'Free'})
    l = 0

    if param == 'start_game':
        return render(request, "moviemon/worldmap.html", game.dic)

    if param == 'load' and data.pos != 0:
        l = data.set_load(game)

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
    if l:
        rend['loading'] = '/options/load_game/start_game'
    else:
        rend['loading'] = '/options/load_game/load'
    slots = data.get_game_list();
    for key, value in slots:
        rend[key] = slots[key][value]

    return render(request, "moviemon/load_game.html", rend)
