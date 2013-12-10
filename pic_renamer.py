#!/usr/bin/python
import os, shutil, time;

from_dir = raw_input("From directory? ")
if from_dir == '':
	from_dir = os.getcwd();
to_dir = raw_input("Destination directory? C:/Users/rpelton/Pictures ")
if to_dir == '':
	to_dir = "C:/Users/rpelton/Pictures"

for file in os.listdir(from_dir):
	if file != __file__ and os.path.isdir(file) is False and file.endswith(".jpg"):
		month = ""
		sub_dir = ""
		this_dir = ""
		new_file = ""
		created = ""

		#	        3    5 ---7---  8
		# format is Tue Oct  7 14:00:00 2013
		created = time.ctime(os.path.getctime(file))
		split = re.split("([A-z0-9\:]+)\s", created)
		if split[3] == 'Jan':
			month = "01 - January"
		elif split[3] == 'Feb':
			month = "02 - February"
		elif split[3] == 'Mar':
			month = "03 - March"
		elif split[3] == 'Apr':
			month = "04 - April"
		elif split[3] == 'May':
			month = "05 - May"
		elif split[3] == 'Jun':
			month = "06 - June"
		elif split[3] == 'Jul':
			month = "07 - July"
		elif split[3] == 'Aug':
			month = "08 - August"
		elif split[3] == 'Sep':
			month = "09 - September"
		elif split[3] == 'Oct':
			month = "10 - October"
		elif split[3] == 'Nov':
			month = "11 - November"
		elif split[3] == 'Dec':
			month = "12 - December"

		sub_dir = split[8] + '/' + month
		this_dir = os.path.join(to_dir, sub_dir)
		if os.path.isdir(this_dir) is False:
			os.makedirs(this_dir)

		print "Move " + file + ". To " + this_dir
		shutil.move(file, this_dir)

