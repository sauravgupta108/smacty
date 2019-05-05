from dashboard.base.base import Base
import os
import json
import requests


class HandleApiRequest(Base):
	def __init__(self, entity, get_list, entity_id=None):
		self.entity = entity
		self.list = get_list
		self.entity_id = entity_id

		self.__base_url = None
		self.__relative_url = None

	def set_base_url(self):
		with open(os.path.join(os.getcwd(), "config/api_config.json"), 'r') as api_config:
			api_conf = json.load(api_config)
			self.__base_url = "%s:%d/%s/" % (api_conf["url"], api_conf["port"], api_conf["name"])

	def set_relative_url(self):		
		if self.entity == "light":
			if self.list and not self.entity_id:
				self.__relative_url = "street_lights"
			elif self.entity_id:
				self.__relative_url = "street_light/%s/" % (self.entity_id)
			else:
				self.__relative_url = None

		elif self.entity == "dustbin":
			if self.list and not self.entity_id:
				self.__relative_url = "dustbins"
			elif self.entity_id:
				self.__relative_url = "dustbin/%s/" % (self.entity_id)
			else:
				self.__relative_url = None

		elif self.entity == "water_tank":
			if self.list and not self.entity_id:
				self.__relative_url = "water_tanks"
			elif self.entity_id:
				self.__relative_url = "water_tank/%s/" % (self.entity_id)
			else:
				self.__relative_url = None
		else:
			self.__relative_url = None

	def make_api_call(self, params=None):
		response = requests.get(url="%s%s" % (self.__base_url, self.__relative_url), params=params)

		# Return dictionary of JSON data recieved via API request
		return json.loads(response.text)
		
	def api_response_post(self):
		pass

	def api_response_get(self, filter_params={}):
		self.set_base_url()
		self.set_relative_url()

		if self.__relative_url and self.__base_url:
			return self.make_api_call(filter_params)
		else:
			return None
				

if __name__ == '__main__':
	params  = {}
	obj = HandleApiRequest("light", get_list=True, entity_id=None)
	if self.request.method == "GET":
		response = obj.api_response_get(params)
	elif self.request.method == "POST":
		obj.api_response_post(params)
