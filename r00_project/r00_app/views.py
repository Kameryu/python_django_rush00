from django.shortcuts import render

# Create your views here.

def titlescreen(request):
	return render(request, "r00/titlescreen.html")

def worldmap(request):
	return render(request, "r00/worldmap.html")

def battle(request):
	
	return render(request, "r00/battle.html", {'ttl' : })

def moviedex(request):
	return render(request, "r00/moviedex.html")

def detail(request):
	return render(request, "r00/detail.html")

def option(request):
	return render(request, "r00/option.html")

def save(request):
	return render(request, "r00/save.html")

def load(request):
	return render(request, "r00/load.html")
