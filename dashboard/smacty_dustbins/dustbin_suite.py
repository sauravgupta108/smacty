from django.http import JsonResponse

from dashboard.base.base import Base
from dashboard.api_handler.api_handler import HandleApiRequest

class Dustbin(Base):
	def __init__(self, request):
		self.request = request
		self.__entity = "dustbin"

	def dustbins(self):	
		variables = {}
		params = {}

		api_client = HandleApiRequest(entity=self.__entity, get_list=True)
		summary = api_client.api_response_get(params)
		
		variables["TotalDustbins"] = len(summary)
		variables["Full"] = len( [i for i in summary if i["filled_status"]] )
		variables["NotFull"] = len( [i for i in summary if not i["filled_status"] ])

		try:
			if "filled_status" in self.request.GET:
				if int(self.request.GET["filled_status"]) in [0,1]:
					params["fs"] = bool(int(self.request.GET["filled_status"]))

			if "street_number" in self.request.GET:
				if int(self.request.GET["street_number"]) < 1:
					raise ValueError
				params["sn"] = int(self.request.GET["street_number"])

			if 'zone' in self.request.GET:
				params["zn"] = self.request.GET["zone"]

			# Get filtered data from API via APIHandler
			api_response = api_client.api_response_get(params)

			if api_response:
				variables["APIData"] = api_response
			else:
				variables["APIError"] = "ApiError"

		except ValueError:
			variables["ErrorMsg"] = "Invalid Input(s)"
			self.log("error", e)
		except Exception as e:
			self.log("error", e)
		return  self.render("dashboard/smacty_dustbins/all_dustbins.html", variables)

	def dustbin(self, dustbin_id):
		pass
