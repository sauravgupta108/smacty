from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from dashboard.smacty_dustbins.dustbin_suite import Dustbin


@login_required
def all_dustbins(request):
	return Dustbin(request).dustbins()

@login_required
def dustbin_details(reuqest, dustbin_id):
	return Dustbin(request).dustbin(ldustbin_id)