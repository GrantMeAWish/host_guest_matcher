max_guests = {'Apartment': 4, 'Suite': 3, 'Dorm': 2}

class Guest(object):

	def __init__(self, name, email, phone, gender, major, major_categ):
		self.name = name
		self.email = email
		self.phone = phone
		self.gender = gender
		self.feats = dict()
		self.feats["major"] = major
		self.feats["major_categ"] = major_categ

	def get_feat(self, feat):
		return self.feats[feat]

class Host(object):

	def __init__(self, name, email, phone, gender, major, major_categ, build_type):
		self.name = name
		self.email = email
		self.phone = phone
		self.gender = gender
		self.feats = dict()
		self.feats["major"] = major
		self.feats["major_categ"] = major_categ

		self.guests = []
		self.max_guests = max_guests[build_type]
		self.full = False

	def add_guest(self, guest):
		self.guests.append(guest)

	def get_feat(self, feat):
		return self.feats[feat]

	def get_guests(self):
		return self.guests

	def print_guests(self):
		guests_string = ''
		
		for guest in self.guests:
			guests_string = guest.name + ', '

		print(guests_string)
