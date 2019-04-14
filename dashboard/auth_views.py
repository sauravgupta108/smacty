from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def auth_login(request):
	variables = {}
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]		

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				variables["LoggedIn"] = True
				return HttpResponseRedirect(reverse('dashboard:home')) if 'next' not in request.GET else HttpResponseRedirect(request.GET["next"])
			else:
				return HttpResponse("Inactive account...!!!!!")
		else:
			variables["InvalidCredentials"] = True

	return render(request, 'registration/login.html', variables)

@login_required
def auth_logout(request):
	logout(request)
	return render(request, 'registration/login.html', {"LoggedOut": True})