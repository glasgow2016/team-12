from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from helixapp.models import tree
import random

pc=0
questDict={1: "Which is the device that has a camera", 2: "Which is the device that doesn't have a camera"}
savedRiddlesDict={}

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

def getRandomSecurityKey():
	global savedRiddlesDict
	key = random.randint(10000 , 99999)
	while(savedRiddlesDict.has_key(str(key))):
		key = random.randint(10000 , 99999)
	
	return str(key)
	
def game_instructions(request):
	return render(request,'helixapp/game/instructions.html')

	
	
def game_new(request):
	global questDict
	global savedRiddlesDict
	x = random.choice(questDict.keys())
	key = getRandomSecurityKey()
	context_dict = {"code": key,"riddle": questDict[x]}
	savedRiddlesDict[key] = x
	return render(request,'helixapp/game/riddle.html' , context_dict)

	
def game_solve(request):
	global savedRiddlesDict
	if request.method == "POST":
		securityCode = request.POST.get("security_code" , "")
		if	savedRiddlesDict.has_key(securityCode):
			location = savedRiddlesDict[securityCode]
			if location == pc:
				x = random.choice(questDict.keys())
				context_dict = {"code": securityCode,"riddle": questDict[x]}
				savedRiddlesDict[securityCode] = x
				return render(request,'helixapp/game/riddle.html' , context_dict)		
	return render(request,'helixapp/game/solve.html')
	
	
