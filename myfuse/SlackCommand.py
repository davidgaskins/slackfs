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
		for key,value in parameters.items():
			url_parameters += "&" + key +"=" + value
		return self.base_url + url_parameters 
class SlackFile(object):
	"""pack and unpack a channel name"""
	def __init__(self, path):
		path = path.strip('/').split('.')
		name = path[0].split('_')
		self.name = name[0]
		self.id = name[1]
		self.type = path[1]
	def _contents(self):
		commands = {"chat":"channels.history", "pins":"pins.list", "files":"files.list", "info":"channels.info"}
		#fetch data
		url_results = SlackCommand(commands[self.type]).get_url({"channel":self.id})
		channel_contents = []
		if self.type == "chat":
			messages = url_results.get("messages")
			for message in messages:
				#identify user
				if message.get("username") is None:
					user = SlackCommand("users.info").get_url({"user":message.get("user")}).get("user").get("name")
				else:
					user = message.get("username")
				#append the contents to an array
				channel_contents.append('\"{}\"-{}'.format(message.get("text"),user))			
		elif self.type == "pins":
			pass
		elif self.type == "files":
			pass
		elif self.type == "info":
			pass
		#join all the text all at once
		return "\n".join(channel_contents)

if __name__ == '__main__':
	command = SlackCommand("channels.list")
	# url_params = {"channel":"C0MA6SXPW"}
	returned = command.get_url({})
	channels = returned.get("channels")
	for channel in channels:
		print(channel.get("id"), channel.get("name"))
	