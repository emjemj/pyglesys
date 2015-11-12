class Email:
	client = None

	optional_arguments = [
		"antispamlevel",
		"antivirus",
		"autorespond",
		"autorespondsaveemail",
		"autorespondmessage",
		"password",
		"quota"
	]

	def __init__(self, client):
		self.client = client

	def overview(self):
		return self.client.get("/email/overview")

	def globalquota(self, quota = None):

		data = None
		if(quota == None):
			data = self.client.post_request("/email/globalquota")
		else:
			data = self.client.post_request("/email/globalquota", 
				{ "globalquota": quota })
		
		return data["globalquota"]

	def list(self, domain):
		data = self.client.get_request("/email/list", 
			{ "domainname": domain })

		return {
			"accounts": data["list"]["emailaccounts"],
			"aliases": data["list"]["emailaliases"]
		}

	def createaccount(self, email, password, extra = None):
		
		if(extra != None):
			for k in extra:
				if k not in self.optional_arguments:
					raise Exception(
						"Invalid parameter: %s " % k)
			params = extra
		else:
			params = {}

		if(email is None or email == ""):
			raise Exception("Please supply email address")

		if(password is None or password == ""):
			raise Exception("Please supply password")

		params["emailaccount"] = email
		params["password"] = password

		data = self.client.post_request("/email/createaccount", params)
		
		return data["emailaccount"]

	def editaccount(self, email, params):
		
		for k in params:
			if k not in self.optional_arguments:
				raise Exception("Invalid parameter: %s" % k)

		if(email is None or email == ""):
			raise Exception("Please supply email address")

		params["emailaccount"] = email

		data = self.client.post_request("/email/editaccount", params)

		return data["emailaccount"]

	def delete(self, email):
		
		if(email is None or email == ""):
			raise Exception("Please supply email address")
		self.client.post_request("/email/delete", { "email": email })

	def quota(self, email):
		
		if(email is None or email == ""):
			raise Exception("please supply email address")

		data = self.client.post_request("/email/quota",
			{ "emailaccount": email })

		return data["emailaccount"]

