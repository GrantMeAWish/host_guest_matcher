import pdb

class Matcher(object):

	def __init__(self, hosts, unpaired):
		self.hosts = hosts
		self.unpaired = unpaired
		self.paired = []

	def get_hosts(self):
		return self.hosts

	def get_unpaired(self):
		return self.unpaired

	def match(self, feat):
		
		for guest in self.unpaired:
			potential_hosts = []

			for host in self.hosts:
				if host.gender != guest.gender or host.full:
					continue

				if feat == 'random' or host.get_feat(feat) == guest.get_feat(feat):
					potential_hosts.append(host)

			if len(potential_hosts) > 0:
				host = min(potential_hosts, key=lambda curr_host: len(curr_host.guests))
				host.add_guest(guest)

				if len(host.guests) >= host.max_guests:
					host.full = True

				self.paired.append(guest)

			
		for guest in self.paired:
			if guest in self.unpaired:
				self.unpaired.remove(guest)
