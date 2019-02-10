from django.http import JsonResponse, HttpResponse

from dashboard.base.base import Base


class Light(Base):
	def __init__(self, request):
		self.request = request

	def lights(self):
		variables = {}
		params = {}
		variables["total_lights"] = 14
		variables["runnig_lights"] = 10
		variables["health_ok"] = 13

		variables["params"] = str(self.request.GET)
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

			# Get data from API via APIHandler
			pass

		except ValueError:
			variables["error_msg"] = "Invalid Input(s)"

		return  self.render("dashboard/smacty_lights/all_lights.html", variables)
		
