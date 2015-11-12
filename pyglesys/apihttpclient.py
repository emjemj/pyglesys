import requests

class APIHTTPClient:
	
	username = None
	apikey = None
	url = "https://api.glesys.com"

	def __init__(self, username, apikey):
		if(username == None or username == ""):
			raise Exception("Please supply a username")
		
		if(apikey == None or apikey == ""):
			raise Exception("please supply an API Key")

		self.username = username
		self.apikey = apikey
	
	def get_request(self, uri, params = {}):
		return self.send_request("GET", uri, params)

	def post_request(self, uri, params = {}):
		return self.send_request("POST", uri, params)

	def send_request(self, method, uri, params):

		if( method not in ("GET", "POST")):
			raise Exception("Invalid HTTP Method: %s" % method)

		url = "%s/%s" % (self.url, uri)
		r = None
		if(method == "POST"):
			url = "%s/format/json" % url
			r = requests.post(url, data = params, auth=(self.username, self.apikey)) 
		elif(method == "GET"):
			for key, value in params.iteritems():
				url = "%s/%s/%s" % (url, key, value)

			url = "%s/format/json" % url 
			r = requests.get(url, auth=(self.username, self.apikey))

		ans =  r.json()

		if(int(ans["response"]["status"]["code"]) != 200):
			raise Exception(ans["response"]["status"]["code"])

		return ans["response"]

