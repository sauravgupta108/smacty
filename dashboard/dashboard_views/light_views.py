from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from dashboard.smacty_lights.light_suite import Light


@login_required
def all_lights(request):
	return Light(request).lights()

@login_required
def light_details(reuqest, light_id):
	pass