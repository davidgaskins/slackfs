#!/usr/bin/python3
import requests
class SlackCommand(object):
	"""Makes a call to the slack api"""
	def __init__(self, api_name):
		#read the credential file
		credentials = open('../credentials.hideme', 'r').readline()
		token = credentials.split("=")[1]
		#define the base api url to hit with requests
		slack_url = "https://slack.com/api/" + api_name
		self.base_url = slack_url + "?token=" + token
	#take in the parameters to hit slack with, return the resulting json
	def get_url(self, parameters):
		results = requests.get(self.form_url(parameters))
		return results.json()
	#take in a dictionary of parameters of parameters to hit slack with, return the url
	def form_url(self, parameters):
		url_parameters = ""
		for key,value in parameters.iteritems():
			url_parameters += "&" + key +"=" + value
		return self.base_url + url_parameters 

if __name__ == '__main__':
	command = SlackCommand("channels.history")
	url_params = {"channel":"C0MA6SXPW"}
	print (command.get_url(url_params))
	