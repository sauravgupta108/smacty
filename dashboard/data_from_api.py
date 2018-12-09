from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, os, json
import logging

class Data_via_api:
	def __init__(self):
		pass

	def tab_data(self, request, tab):
		with(open(os.path.join(os.getcwd(), "config/api_config.json"), 'r')) as api:
			config = json.load(api)

		param = dict(request.GET)
						
		url = config["url"] + ":" + str(config["port"]) + "/" + config["name"] + "/"
		if tab == 'lights':
			url+="street_lights"
		elif tab == 'dustbins':
			url+='dustbins'
		elif tab == 'water_tanks':
			url+= 'water_tanks'
		
		api_response = requests.get(url = url, params = param)

		logging.basicConfig(filename='logs/access.log', level=logging.DEBUG)
		# logging.info(filename='logs/access.log', api_response.url)
		
		return api_response.json()
		
		# return render(request, "dashboard/tab_contents.html" , content)