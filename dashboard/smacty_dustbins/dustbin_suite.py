from django.http import JsonResponse

from dashboard.base.base import Base

class Dustbin(Base):
	def __init__(self, request):
		self.request = request

	def dustbins(self):		
		return  self.render("dashboard/about.html")