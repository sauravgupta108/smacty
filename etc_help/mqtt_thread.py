import threading, json, time
import paho.mqtt.client as mqtt

from . import mqtt_client as mq_clnt

class Mqtt_Thread(threading.Thread):
	'''This class runs MQTT Clients as Threads.'''
	def __init__(self, name, client_type):
		threading.Thread.__init__(self)
		self._name = name
		self._MQTT_CLIENT = mq_clnt.Mqtt_Client(mqtt.Client(client_id = self._name))
		self.pub_rslt = False

		if client_type not in ('PUB', 'SUB'):
			raise ValueError("Invalid Client Type")
		else:
			self._client_type = client_type

	def start(self, topic = "", message = ""):
		if len(topic.split('/')) < 2:
			raise ValueError("Invalid Topic")
		else:
			self._topic = topic

		if (self._client_type == 'PUB'):
			if (message == ""):
				raise ValueError("Message can not be empty.")
			else:
				self._pub_message = message

		threading.Thread.start(self)

	def disconnect(self):  #Use it only for subscriber, not for publisher.
		self._MQTT_CLIENT.disconnect_from_broker()

	def run(self):
		if self._client_type == 'PUB':
			'''This method will run the mqtt client (Thread) as Publisher.'''
			self._MQTT_CLIENT.publish_to_broker(self._topic, self._pub_message)
			
		else:
			'''This method will run the mqtt client (Thread) as Subscriber.'''
			self._MQTT_CLIENT.subscribe_topic(self._topic)

	def is_published(self):
		return self._MQTT_CLIENT._pub_result

	def get_subscribed_messages(self):
		return self._MQTT_CLIENT._sub_msgs
