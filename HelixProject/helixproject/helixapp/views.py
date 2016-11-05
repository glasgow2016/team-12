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
	
def gameInstructions(request):
	return render(request,'helixapp/game/instructions.html')

def gameNew(request):
	return render(request,'helixapp/game/new.html')

def gameRiddle(request):
	return render(request,'helixapp/game/riddle.html')
	
	