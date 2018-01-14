from django.conf import settings
import pickle, random, requests, json

class MovieMonData:

    def __init__(self):
        self.dic = {}

    class Movie:
        def __init__(self, title, idimdb, rating, poster, director, year, plot, actors):
            self.info = [
                    title,
                    idimdb,
                    rating,
                    poster,
                    director,
                    year,
                    plot,
                    actors,
            ]

    def load(self, name):
        save = open(name, "rb")
        self.dic = pickle.load(save)
        save.close()

    def dump(self, name):
        save = open(name, "wb")
        pickle.dump(self.dic, save)
        save.close()

    def get_random_movie(self):
        nb = len(self.dic['movies_to_catch'])
        i = (random.randint(0, nb - 1))
        return self.dic['movies_to_catch'][i].info

    def load_default_settings(self):
        
        movies = []
        for idimdb in settings.MOVIES:
            result = requests.get("http://www.omdbapi.com/?i=" + idimdb + "&apikey=d5596361").json()
            if 'error' in result:
                raise Exception(result['error'])
            if 'warnings' in result:
                print("warning : " + result['warnings'])
            title = result['Title']
            poster = result['Poster']
            director = result['Director']
            year = result['Year']
            rating = result['imdbRating']
            plot = result['Plot']
            actors = result['Actors']
            tmp = self.Movie(title, idimdb, rating, poster, director, year, plot, actors)
            movies.append(tmp)

        self.dic = {
            'sizex' : list(range(settings.MAPSIZE[0])),
            'sizey' : list(range(settings.MAPSIZE[1])),
            'pos' : settings.PLAYER_START_POSITION,
            'movies_to_catch' : movies,
            'movies_in_pocket' : [],
            'ball' : settings.NBBALLS,
            'found' : [False],
            'encounter' : [False]
        }

    def get_strength(self):
        print("todo")

    def get_movie(self, idimbd):
        print("todo")

    def is_moving(self):
        print("movies restants :", len(self.dic['movies_to_catch']))
        print("movies attrapes :", len(self.dic['movies_in_pocket']))
        chance = (random.randint(1,100))
        if chance > 30:
            self.dic['found'] = [True]
            self.dic['ball'] += 1
        else:
            self.dic['found'] = [False]

        if len(self.dic['movies_to_catch']) > 0:
            chance = (random.randint(1,100))
            if chance > 30:
                self.dic['encounter'] = [True, self.get_random_movie(), False]
            else:
                self.dic['encounter'] = [False]

