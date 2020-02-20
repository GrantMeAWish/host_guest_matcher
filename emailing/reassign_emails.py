import yagmail
import csv

filename = "reassign.csv"

yag = yagmail.SMTP("berkeleyrohp@gmail.com")

dates = ["February 22", "March 8", "March 9", "March 15", "March 16", "April 12"]

date = input("Please enter the number of which ROHP night you are matching for:\n \
0: February 22\n \
1: March 8\n \
2: March 9\n \
3: March 15\n \
4: March 16\n \
5: April 12\n")

subject = "UPDATE: ROHP " + dates[int(date)] + " Host Guest Re-Matching"

with open(filename, "r") as csvfile:

	reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL);

	for row in reader:

		# Format of each row is:

		# 0. Old host name,
		# 1. Old host email,
		# 2. Old host phone #,
		# 3. New host name,
		# 4. New host email,
		# 5. New host phone #,
		# 6. Guest name,
		# 7. Guest email,
		# 8. Guest phone #,

		guest = {}
		old_host = {}
		new_host = {}

		old_host["name"] = row[0]
		old_host["email"] = row[1]
		old_host["phone"] = row[2]

		new_host["name"] = row[3]
		new_host["email"] = row[4]
		new_host["phone"] = row[5]

		guest["name"] = row[6]
		guest["email"] = row[7]
		guest["phone"] = row[8]

		receiver = {guest["email"]: guest["name"], old_host["email"]: old_host["name"], new_host["email"]: new_host["name"]}


		body = "Hello, \n\n\
		Due to some logistical hiccups, you've been reassigned to a new host/guest. Please ignore your previous assignment. Below, you can find each other’s contact information. \n \
		\n\n \
		Previous assignment that is no longer valid: \n \
		" + guest["name"] + ", " + guest["email"] + ", " + guest["phone"] + "\n" \
		+ old_host["name"] + ", " + old_host["email"] + ", " + old_host["phone"] + "\n" \
		+ "\n\n \
		NEW assignment: \n \
		" + guest["name"] + ", " + guest["email"] + ", " + guest["phone"] + "\n" \
		+ new_host["name"] + ", " + new_host["email"] + ", " + new_host["phone"] + "\n\n" \
		"We apologize for any confusion that is caused by this, so feel free to email us at contact@rohp.berkeley.edu if you have any questions." \
		+ "\n\n"

		html = "<span style=\"background-color:rgb(0,0,0)\"> \
				<b>\
				<font color=\"#6fa8dc\">G</font> \
				<font color=\"#ffd966\">O</font> \
				<span>&nbsp;</span> \
				<font color=\"#6fa8dc\">B</font> \
				<font color=\"#ffd966\">E</font> \
				<font color=\"#6fa8dc\">A</font> \
				<font color=\"#ffd966\">R</font> \
				<font color=\"#6fa8dc\">S</font> \
				<font color=\"#ffd966\">,</font> \
				</b> \
				</span>"

		signoff = "ROHP Committee 2019"

		print("Guest: " + guest["name"] + ", Old: " + old_host["name"] + ", New: " + new_host["name"])

		yag.send(
		    to=receiver,
		    subject=subject,
		    contents=[body, html, signoff, dates[int(date)] + " ROHP Schedule.pdf", "Important Resources.zip"]
		) 
