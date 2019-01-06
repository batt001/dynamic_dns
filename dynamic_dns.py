import requests
import json
import threading
import time
import datetime

class dynamicDNS(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.username='batt001.master@gmail.com'
		self.password='batt91221'
		self.hostname='sajtostejfolos.ydns.eu'
		self.delay=1800
		self.previous_ip='not defined'
		self.current_ip='not defined'
	def run(self):
		while True:
			self.update_hostname()
			time.sleep(delay)
			
	def update_hostname(self):
		""" If IP address changed update the hostname with current IP"""
		if (self.ip_changed()):
			timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			print(timestamp + " Ip changed, current ip: " + self.current_ip + " updating hostname: " + self.hostname + " ...")
			update_ip_response = requests.get('https://ydns.io/api/v1/update/?host=' + self.hostname + '&ip=' + self.current_ip, auth=(self.username, self.password))
			self.previous_ip = self.current_ip

	""" Check if IP has changed """
	def ip_changed(self):
		get_current_ip_response = requests.get('https://ydns.io/api/v1/ip.json')
		self.current_ip = json.loads(get_current_ip_response.text)['ip']
		if (self.current_ip != self.previous_ip):
			return True
		else:
			return False

ddns_thread = dynamicDNS()
ddns_thread.start()