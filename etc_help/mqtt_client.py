#import paho.mqtt.client as mqtt
import json, time, os

class Mqtt_Client:

	def __init__(self, client_mqtt):
		self.mqtt_client = client_mqtt
		self._connection_ok = False		
		self._pub_result = False
		self._sub_result = False
		self._sub_msgs = []
		self._qos = 0

	def on_connect(self, client, userdata, flags, rc):
		if rc != 0:
			raise RuntimeError("MQTT Broker connection failed.")
		else:
			self._connection_ok = True
			
	def on_disconnect(self, client, userdata, flags):
		self.mqtt_client.loop_stop()
		self._connection_ok = False

	def on_log(self, client, userdata, level, buf):
		print("Log: " + buf)

	def on_publish(self, client, userdata, mid):
		self._pub_result = True
	
	def on_subscribe(self, client, userdata, mid, granted_qos):
		self._sub_result = True

	def on_message(self, client, userdata, message):
		time.sleep(0.3)
		self._sub_msgs.append(str(message.payload))

	def get_mqtt_broker_details(self):
		mqtt_broker = None
		try:
			path = os.getcwd()
			with open(os.path.join(path,'config/mqtt_config.json'), "r") as config_file:
				mqtt_broker = json.load(config_file)
				self._qos = int(mqtt_broker["qos"])
				return mqtt_broker
		except:
			raise RuntimeError("Could not get Broker details.")

		print(self._qos)
			
	def connect_broker(self):
		'''Connects to MQTT broker and returns a MQTT Client object.'''
		broker_details = self.get_mqtt_broker_details()

		self.mqtt_client.username_pw_set(broker_details['USERNAME'], broker_details['PASSWORD'])

		self.mqtt_client.on_connect = self.on_connect
		self.mqtt_client.on_disconnect = self.on_disconnect
		self.mqtt_client.on_publish = self.on_publish
		self.mqtt_client.on_subscribe = self.on_subscribe
		self.mqtt_client.on_message = self.on_message
		#self.mqtt_client.on_log = self.on_log
		
		try:
			self.mqtt_client.connect(broker_details['HOST'], broker_details['PORT'], broker_details['keepalive'])
		except:		
			#del self.mqtt_client
			raise RuntimeError("MQTT Broker connection failed.")
		
		time.sleep(0.2)

	def publish_to_broker(self, topic, message):
		self.connect_broker()
		
		self.mqtt_client.loop_start();time.sleep(0.5)		
		self.mqtt_client.publish(topic = topic, payload = str(message), qos = self._qos)
		time.sleep(0.1)
		
		if self._connection_ok or self._pub_result:
			self.disconnect_from_broker()

	def subscribe_topic(self, topic):
		self.connect_broker()
		try:
			self.mqtt_client.subscribe(topic, qos = self._qos)
		except:
			raise RuntimeError("Unable to subscribe: ", topic)

		self.mqtt_client.loop_forever()

	def disconnect_from_broker(self):
		self.mqtt_client.disconnect()
		time.sleep(0.1)
