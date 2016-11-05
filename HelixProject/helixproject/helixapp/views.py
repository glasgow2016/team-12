from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
    if request.method=='POST':
		return render(request,'helixapp/index.html')
    else:
		return render(request,'helixapp/index.html')

	
def game(request):
	return render(request,'helixapp/game.html')
	
def game_instructions(request):
	return render(request,'helixapp/game/instructions.html')

def game_new(request):
	return render(request,'helixapp/game/riddle.html')

def game_riddle(request):
	return render(request,'helixapp/game/riddle.html')
	
	