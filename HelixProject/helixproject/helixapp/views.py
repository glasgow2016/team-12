from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from helixapp.models import tree

pc=0

def index(request):
    global pc

    response = render(request,'helixapp/index.html')  # django.http.HttpResponse
    try:
        value=request.COOKIES[str(pc)]
    except:
        pc=pc+1
        response.set_cookie(str(pc), pc)
    return response

def getTree():
    for t in tree.objects.all():
        if t.isTaken==False:
            t.isTaken=True
            t.save()
            break
    return t
	
def game(request):
	return render(request,'helixapp/game.html')
	
def game_instructions(request):
	return render(request,'helixapp/game/instructions.html')

def game_new(request):

                
	return render(request,'helixapp/game/riddle.html')

def game_riddle(request):
	return render(request,'helixapp/game/riddle.html')
	
	
