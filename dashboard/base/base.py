from django.template.loader import render_to_string
from django.http import HttpResponse


class Base:
	def __init__(self):
		pass

	def log(self, level, msg=None):
		import logging
		dev_logger = logging.getLogger("dev")
		
		if level.lower().strip() == "debug":
			dev_logger.debug(msg)

		elif level.lower().strip() == "info":
			dev_logger.info(msg)

		elif level.lower().strip() == "warning":
			dev_logger.warning(msg)

		elif level.lower().strip() == "error":
			dev_logger.error(msg, exc_info = True)

		elif level.lower().strip() == "critical":
			dev_logger.critical(msg, exc_info = True)

		else:
			dev_logger.log(5, msg)

	def render(self, template_name=None, variables=None):
		return HttpResponse(render_to_string(template_name, context=variables))
		