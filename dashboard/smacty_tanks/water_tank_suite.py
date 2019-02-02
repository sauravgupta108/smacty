from django.http import JsonResponse

from dashboard.base.base import Base

class Tank(Base):
	def __init__(self, request):
		self.request = request

	def tanks(self):		
		return  self.render("dashboard/about.html")