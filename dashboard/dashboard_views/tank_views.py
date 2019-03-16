from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from dashboard.smacty_tanks.water_tank_suite import Tank

@login_required
def all_water_tanks(request):
	return Tank(request).tanks()

@login_required
def water_tank_details(reuqest, tank_id):
	pass