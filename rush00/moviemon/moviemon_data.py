from django.conf import settings
import pickle, random, requests, json

class MovieMonData:

    def __init__(self):
        self.dic = {}

    def load(self, name):
        save = open(name, "rb")
        self.dic = pickle.load(save)
        save.close()

    def dump(self, name):
        save = open(name, "wb")
        pickle.dump(self.dic, save)
        save.close()

    def get_random_movie(self):
        print("todo")

    def load_default_settings(self):
        
        for movie in settings.MOVIES:
            result = requests.get("http://www.omdbapi.com/?i=" + movie + "&apikey=d5596361").json()
            if 'error' in result:
                raise Exception(result['error'])
            if 'warnings' in result:
                print("warning : " + result['warnings'])
            print(result['Title'])
            print(result['Poster'])
            print(result['Director'])
            print(result['Year'])
            print(result['imdbRating'])
            print(result['Plot'])
            print(result['Actors'])


        self.dic = {'sizex' : list(range(settings.MAPSIZE[0])), 'sizey' : list(range(settings.MAPSIZE[1])), 'pos' : settings.PLAYER_START_POSITION, 'movies' : settings.MOVIES, 'ball' : settings.NBBALLS}
        

    def get_strength(self):
        print("todo")

    def get_movie(self):
        print("todo")

    def is_moving(self):
        chance = (random.randint(1,100))
        if chance > 70:
            self.dic['found'] = [True]
            self.dic['ball'] += 1
        else:
            self.dic['found'] = [False]

        chance = (random.randint(1,100))
        if chance > 70:
            self.dic['encounter'] = [True, "Name", 42]
        else:
            self.dic['encounter'] = [False]

