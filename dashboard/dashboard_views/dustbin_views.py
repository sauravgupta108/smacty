from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from dashboard.smacty_dustbins.dustbin_suite import Dustbin


def all_dustbins(request):
	return Dustbin(request).dustbins()

def dustbin_details(reuqest, dustbin_id):
	pass