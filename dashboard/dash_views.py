from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from etc_help.mqtt_thread import Mqtt_Thread
import json, time, os

# Create your views here.
def index(request):
	return render(request,'dashboard/index.html')

def publish(request):
	if request.method == "POST":
		topic = request.POST["topic"]
		message = request.POST["message"]
		out_put = {}
		out_put["result"] = "Error...."

		pub_obj = Mqtt_Thread('Thread-PUB-1', 'PUB')
		pub_obj.start(topic, message)
		pub_obj.join()
		
		if pub_obj.is_published():
			out_put["result"] = str(message) + " published to topic " + str(topic)

		return HttpResponse(json.dumps(out_put), content_type="application/json")

	else:
		return HttpResponse("get")

def subscribe(request):
	if request.method == "POST":
		out_put = {}
		out_put["result"] = request.POST["topic"]
		
		sub_obj = Mqtt_Thread("Thread-SUB-1", "SUB")
		sub_obj.start(request.POST["topic"])

		with(open(os.path.join(os.getcwd(), "config/subscribe_prop.json"),'r')) as tm:
			dta = json.load(tm)

		time.sleep(dta["waiting_time"])
		sub_obj.disconnect()
		out_put["result"] = sub_obj.get_subscribed_messages()

		return HttpResponse(json.dumps(out_put), content_type="application/json")