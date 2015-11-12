class Changelog:
	client = None

	def __init__(self, client):
		self.client = client

	def api(self):
		return self.client.get_request("/changelog/api")
	def controlpanel(self):
		return self.client.get_request("/changelog/controlpanel")
