from django.http import JsonResponse

from dashboard.base.base import Base

class Light(Base):
	def __init__(self, request):
		self.request = request

	def lights(self):		
		return  self.render("dashboard/about.html")