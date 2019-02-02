from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from dashboard.smacty_tanks.water_tank_suite import Tank

def all_water_tanks(request):
	return Tank(request).tanks()

def water_tank_details(reuqest, tank_id):
	pass