from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models
from login.models import Person
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from login.forms import HandsForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/main/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
	user = request.user
	print(user, user.is_authenticated)
	if not request.user.is_authenticated:
		return redirect("/")
	else:
		form = HandsForm(request.GET)
		leaderboard = Person.objects.all().order_by('-hands_cnt', '-hands_cnt')
		return render(request, "leaderboard.html", {'players': leaderboard, 'form': form})

def addUser(request, username="Screloma", hands_cnt=0, hrs_cnt=0):
	leaderboard = Person.objects.all()
	if request.method == 'POST':
		form = HandsForm(request.POST)
		leaderboard = Person.objects.all().order_by('-hrs_cnt', '-hands_cnt')
		if str(request.user) not in [player.name for player in leaderboard]:
			if(len(request.POST['hands_cnt'])!=0 and len(request.POST['hrs_cnt'])!=0):
				newhands = Person(name=request.user, hands_cnt=request.POST['hands_cnt'], hrs_cnt=request.POST['hrs_cnt'])
				newhands.save()
			else:
				return redirect('/main')
		else:
			player = Person.objects.get(name=str(request.user))
			print(player.hands_cnt, player.hrs_cnt)
			if(len(request.POST['hands_cnt'])!=0):
				player.hrs_cnt += int(request.POST['hands_cnt'])
			if(len(request.POST['hrs_cnt'])!=0):
				player.hands_cnt += int(request.POST['hrs_cnt'])
			player.save()
	else:
		form = HandsForm(request)
	return redirect('/main/')
