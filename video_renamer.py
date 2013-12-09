#!/usr/bin/python
import os, shutil, time;

from_dir = raw_input("From directory? ")
if from_dir == '':
	from_dir = os.getcwd();
to_dir = raw_input("Destination directory? C:/Users/rpelton/Pictures ")
if to_dir == '':
	to_dir = "C:/Users/rpelton/Pictures"

for file in os.listdir(from_dir):
	if file != __file__ and os.path.isdir(file) is False:
		month = ""
		sub_dir = ""

		# format is Oct  7 14:00:00 2013
		created = time.ctime(os.path.getctime(file))
		split = created.split(' ')
		if split[1] == 'Jan':
			month = "01"
		elif split[1] == 'Feb':
			month = "02"
		elif split[1] == 'Mar':
			month = "03"
		elif split[1] == 'Apr':
			month = "04"
		elif split[1] == 'May':
			month = "05"
		elif split[1] == 'Jun':
			month = "06"
		elif split[1] == 'Jul':
			month = "07"
		elif split[1] == 'Aug':
			month = "08"
		elif split[1] == 'Sep':
			month = "09"
		elif split[1] == 'Oct':
			month = "10"
		elif split[1] == 'Nov':
			month = "11"
		elif split[1] == 'Dec':
			month = "12"

		sub_dir = split[5] + '/' + month
		this_dir = os.path.join(to_dir, sub_dir)
		if os.path.isdir(this_dir) is False:
			os.makedirs(this_dir)

		print "Move " + file + ". To " + this_dir
		shutil.move(file, this_dir)

