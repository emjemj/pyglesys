class API:
	client = None

	def __init__(self, client):
		self.client = client

	def maintenance(self):
		return self.client.get_request("/api/maintenance")
	
	def serviceinfo(self):
		return self.client.get_request("/api/serviceinfo")
	
	def listfunctions(self):
		return self.client.get_request("/api/listfunctions")
