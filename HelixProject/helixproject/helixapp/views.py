from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from helixapp.models import tree
import random

# pc = unique machine id
pc=0

#only two test devices
# 1 is Laptop
# 2 is Pi
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
	
	#unique key to complete challenges
	key = random.randint(10000 , 99999)
	while(savedRiddlesDict.has_key(str(key))):
		key = random.randint(10000 , 99999)
	
	return str(key)
	
def game_instructions(request):
	return render(request,'helixapp/game/instructions.html')

		
def locations(request):
	locations = {0: {"name": "The laptop with the camera", "address": "0.0.0.0:1212"}}
	context_dict = {"locations" : locations}
	
	return render(request,'helixapp/camera/locations.html' , context_dict)
		
def location(request):
	#context_dict = {"address" : address}
	
	return render(request,'helixapp/camera/location.html')

		
def live(request):
	return render(request,'helixapp/camera/live.html')

			
def selfie(request):
	return render(request,'helixapp/camera/selfie.html')

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
	global pc
	context_dict = {}
	if request.method == "POST":
		context_dict = {"errorMessage" : "You have chosen the wrong location. Please try again!"}
		securityCode = request.POST.get("security_code" , "")
		if	savedRiddlesDict.has_key(securityCode):
			location = savedRiddlesDict[securityCode]
			if str(location) == str(request.COOKIES[str(pc)]):
				x = random.choice(questDict.keys())
				context_dict = {"code": securityCode, "riddle": questDict[x]}
				savedRiddlesDict[securityCode] = x
				return render(request,'helixapp/game/riddle.html' , context_dict)		
			else:
				return render(request,'helixapp/game/wrong.html')
		else:
			return render(request,'helixapp/game/wrong.html')
			
	return render(request,'helixapp/game/solve.html')
	
	
def maps(request):
	return render(request,'helixapp/maps.html')

def history(request):
	return render(request,'helixapp/history.html')

def history_generalInfo(request):
	return render(request,'helixapp/history/generalInfo.html')

def history_current(request):
	return render(request,'helixapp/history/current.html')

def history_favourites(request):
	return render(request,'helixapp/history/favourites.html')

def camera(request):
	return render(request,'helixapp/camera.html')

def activities(request):
	return render(request,'helixapp/activities.html')

def emergency(request):
	return render(request,'helixapp/emergency.html')

def index(request):
	return render(request,'helixapp/index.html')
