from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from dashboard.smacty_lights.light_suite import Light


def all_lights(request):
	return Light(request).lights()

def light_details(reuqest, light_id):
	pass