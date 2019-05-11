from django.http import JsonResponse

from dashboard.base.base import Base

class Dustbin(Base):
	def __init__(self, request):
		self.request = request
		self.__entity = "dustbin"

	def dustbins(self):	
		variables = {}
		params = {}

		# api_client = HandleApiRequest(entity=self.__entity, get_list=True)
		# summary = api_client.api_response_get(params)
			
		return  self.render("dashboard/smacty_dustbins/all_dustbins.html")