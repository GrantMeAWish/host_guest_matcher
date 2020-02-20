import csv
from hgm.student import Guest, Host
from hgm.matcher import Matcher
import pdb
from difflib import SequenceMatcher

def preprocess_csv(filename, student_type):
	students = []

	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0

		for row in csv_reader:
			if line_count == 0:
				line_count += 1
			else:
				if student_type == 'hosts':
					name = row[3]
					email = row[1]
					phone = row[5]
					gender = row[4]
					major = row[9]
					major_categ = row[10]
					build_type = row[12]
					roommates = []
					if row[13] == "Yes":
						roommates = row[14].split(",")
					host = Host(name, email, phone, gender, major, major_categ, build_type, roommates)
					students.append(host)
				else:
					name = row[0]
					email = row[1]
					phone = row[2]
					gender = row[3]
					major = row[4]
					major_categ = row[5]
					guest = Guest(name, email, phone, gender, major, major_categ)
					students.append(guest)

				line_count += 1

	return students

def __similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def __check_roommates(hosts):
	for host in hosts:
		roommates = host.get_roommates()

		for roommate in roommates:
			for host in hosts:
				if __similar(roommate, host.name) > 0.9:
					host.max_guests -= 1

def match(host_csv, guest_csv):
	hosts = preprocess_csv(host_csv, 'hosts')
	guests = preprocess_csv(guest_csv, 'guests')
	__check_roommates(hosts)

	matcher = Matcher(hosts, guests)
	matcher.match("major")
	matcher.match("major_categ")
	matcher.match("random")
	print("unpaired hosts", [host.name + " " + host.gender for host in matcher.get_hosts() if len(host.guests) == 0])

	matched_hosts = matcher.get_hosts()
	unpaired_guests = matcher.get_unpaired()

	return matched_hosts, unpaired_guests

def write_matches(matched_hosts, write_csv_name):
	with open(write_csv_name, mode='w') as csv_file:
		writer = csv.writer(csv_file)

		writer.writerow(["host name", "host email", "host phone", "host gender", \
			"host major", "host major category", "host max room capacity", \
			"guest name", "guest email", "guest phone", "guest gender", \
			"guest major", "guest major category"])

		for host in matched_hosts:
			for guest in host.guests:
				writer.writerow([host.name, host.email, host.phone, host.gender, \
					host.get_feat("major"), host.get_feat("major_categ"), host.max_guests, \
					guest.name, guest.email, guest.phone, guest.gender, \
					guest.get_feat("major"), guest.get_feat("major_categ")])

def write_unpaired(unpaired_guests, write_csv_name):
	with open(write_csv_name, mode='w') as csv_file:
		writer = csv.writer(csv_file)

		writer.writerow(["guest name", "guest email", "guest phone", "guest gender", \
			"guest major", "guest major category"])

		for guest in unpaired_guests:
			writer.writerow([guest.name, guest.email, guest.phone, guest.gender, \
					guest.get_feat("major"), guest.get_feat("major_categ")])
