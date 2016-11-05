from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from helixapp.models import tree
import random

pc=0
questDict={"1": "Which is the device that has a camera", "2": "Which is the device that doesn't have a camera"}

savedRiddles={}

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
	global questDict
	x = random.choice(questDict.keys())
	context_dict = {"code": 123321,"riddle": questDict[x]}
	return render(request,'helixapp/game/riddle.html',context_dict)

def game_riddle(request):
	return render(request,'helixapp/game/riddle.html')
	
	
