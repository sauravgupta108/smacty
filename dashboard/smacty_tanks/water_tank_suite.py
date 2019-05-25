from django.http import JsonResponse

from dashboard.base.base import Base

class Tank(Base):
	def __init__(self, request):
		self.request = request
		self.__entity = "water_tank"

	def tanks(self):		
		variables = {}
		params = {}

		# api_client = HandleApiRequest(entity=self.__entity, get_list=True)
		# summary = api_client.api_response_get(params)
			
		return  self.render("dashboard/smacty_water_tanks/all_water_tanks.html")

	def tank(self, tank_id):
		pass