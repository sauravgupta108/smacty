from django.http import JsonResponse, HttpResponse

from dashboard.base.base import Base
from dashboard.api_handler.api_handler import HandleApiRequest


class Light(Base):
	def __init__(self, request):
		self.request = request
		self.__entity = "light"

	def lights(self):
		variables = {}
		params = {}

		api_client = HandleApiRequest(entity=self.__entity, get_list=True)
		summary = api_client.api_response_get(params)

		variables["TotalLights"] = len(summary)
		variables["Running"] = len([i for i in summary if i["running_status"] ])
		variables["NotHealthy"] = len([i for i in summary if i["health"] != 1 ])
		
		try:
			if 'street_number' in self.request.GET:
				if int(self.request.GET["street_number"]) < 1:
					raise ValueError
				params["sn"] = int(self.request.GET["street_number"])

			if 'health_status' in self.request.GET:
				if int(self.request.GET["health_status"]) != -1:
					params["hlth"] = int(self.request.GET["health_status"])

			if 'running_status' in self.request.GET:
				if int(self.request.GET["running_status"]) != -1:
					params["rs"] = int(self.request.GET["running_status"])

			if 'zone' in self.request.GET:
				params["zn"] = self.request.GET["zone"]

			# Get filtered data from API via APIHandler
			api_response = api_client.api_response_get(params)

			if api_response:
				variables["APIData"] = api_response
			else:
				variables["APIError"] = "ApiError"

		except ValueError as e:
			variables["ErrorMsg"] = "Invalid Input(s)"
			self.log("error", e)
		except Exception as e:
			self.log("error", e)

		return  self.render("dashboard/smacty_lights/all_lights.html", variables)
		
	def light(self, light_id):
		pass
