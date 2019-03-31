import json
import threading
import time
import datetime
import socket
import sys
try:
    import requests
except ImportError:
    print("Requests python module is not installed, please install it (pip)")
    sys.exit(1)


class dynamicDNS(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.username = 'batt001.master@gmail.com'
        self.password = 'batt91221'
        self.hostname = 'sajtostejfolos.ydns.eu'
        self.delay = 1800
        self.previous_ip = 'not defined'
        self.current_ip = 'not defined'
        self.logfile = 'not defined'

    def run(self):
        self.logfile = "log_dynamic_dns_" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + ".log"
        while True:
            if self.check_network_connection():
                self.update_hostname()
            time.sleep(self.delay)

    def update_hostname(self):
        """ If IP address changed update the hostname with current IP"""
        if self.ip_changed():
            self.log("Ip changed, current ip: " + self.current_ip + " updating hostname: " + self.hostname + " ...")

            """ Send new ip to YDNS website """
            requst_url = 'https://ydns.io/api/v1/update/?host=' + self.hostname + '&ip=' + self.current_ip
            requests.get(requst_url, auth=(self.username, self.password))

            """ Set previous_ip to current_ip for next iteration check """
            self.previous_ip = self.current_ip



    def ip_changed(self):
        # Check if IP has changed
        get_current_ip_response = requests.get('https://ydns.io/api/v1/ip.json')
        self.current_ip = json.loads(get_current_ip_response.text)['ip']
        if self.current_ip != self.previous_ip:
            return True
        else:
            return False



    def check_network_connection(self):
        # Check if internet is available
        url_to_check = "ydns.io"
        try:
            socket.create_connection((url_to_check, 80))
            return True
        except OSError:
            self.log("Network or " + url_to_check + " webpage is unavailable")
        return False



    def log(self, message):
        # Writes the message passed as a parameter to the console and the defined logfile

        """ Setup log message """
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " "
        log_message = timestamp + message

        """ Pring log message to console """
        print(log_message)

        """ Write update event into logfile """
        with open(self.logfile, 'a') as logfile:
            logfile.write(log_message + "\n")
            logfile.close()


if __name__ == '__main__':
    ddns_thread = dynamicDNS()
    ddns_thread.start()
