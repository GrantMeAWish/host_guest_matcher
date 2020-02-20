#CHANGE filename 

import yagmail
import csv

filename = "2-21-match.csv" #TODO

yag = yagmail.SMTP("berkeleyrohp@gmail.com")

dates = ["February 21", "March 6", "March 7", "March 13", "March 14", "April 17"]

date = input("Please enter the number of which ROHP night you are matching for:\n \
0: February 21\n \
1: March 6\n \
2: March 7\n \
3: March 13\n \
4: March 14\n \
5: April 17\n")

subject = "ROHP " + dates[int(date)] + " Host Guest Matching"

with open(filename, "r") as csvfile:

	reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL);
	next(reader, None)

	for row in reader:

		guest = {}
		host = {}

		guest["name"] = row[0]
		guest["email"] = row[1]
		guest["phone"] = row[2]

		host["name"] = row[7]
		host["email"] = row[8]
		host["phone"] = row[9]


		receiver = {guest["email"]: guest["name"], host["email"]: host["name"]}


		body = \
		"Hello, \n\n \
		You two have been matched as host and guest for ROHP on " + dates[int(date)] + ". Below, you can find each other’s contact information. \n \
		\n\n \
		" + guest["name"] + ", " + guest["email"] + ", " + guest["phone"] + "\n" \
		+ host["name"] + ", " + host["email"] + ", " + host["phone"] + "\n" \
		+ "\n\n \
		When the day comes, please check in at Unit 2 APR at 5:15 PM. Directions can be found in the attached PDF. \
		Please review rohp.berkeley.edu for information about what to bring, the schedule, and other details. \
		We've also attached the schedule and an important resources folder to this email for your convenience. \
		If you are a host, please remember that you need to show up at 7:45 PM to pick up your guest. \
		\n\n \
		If you have additional questions, don’t hesitate to email us at contact@rohp.berkeley.edu. We look forward to seeing you soon! \
		\n\n \
		P.S. Please check weather conditions in Berkeley a couple of days before your trip and make sure to \
		bring appropriate accommodations (umbrella, closed-toe shoes, raincoat, etc.) if need be and please bring a sleeping bag!\n\n \
		"

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

		signoff = "ROHP Committee 2020"

		print("Sending email to: " + guest["name"] + ", " + host["name"])

		yag.send(
		    to=receiver,
		    subject=subject,
		    contents=[body, html, signoff, dates[int(date)] + " Schedule.pdf", "APR_directions.pdf", "Important Resources.zip"]
		) 
