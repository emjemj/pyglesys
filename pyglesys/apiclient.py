from apihttpclient import APIHTTPClient

from api import API
from changelog import Changelog
from email import Email

class APIClient:
	client = None
	changelog = None

	def __init__(self, username, apikey):
		self.client = APIHTTPClient(username, apikey)
		
		# API Modules
		self.api = API(self.client)
		self.changelog = Changelog(self.client)
		self.email = Email(self.client)
	
