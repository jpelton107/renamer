#!/usr/bin/python
import os, shutil, time, re
default_dir = "H:/Videos/HomeVideos"
file_ext = ".mp4"

from_dir = raw_input("From directory? ")
if from_dir == '':
	from_dir = os.getcwd();
to_dir = raw_input("Destination directory? " + default_dir)
if to_dir == '':
	to_dir = default_dir

for file in os.listdir(from_dir):
	if os.path.isdir(file) is False and file.endswith(file_ext):
		month = ""
		sub_dir = ""
		this_dir = ""
		new_file = ""
		created = ""

		# format is Oct  7 14:00:00 2013
		created = time.ctime(os.path.getctime(file))
		split = re.split("([A-z0-9\:]+)\s", created)
		if split[3] == 'Jan':
			month = "01"
		elif split[3] == 'Feb':
			month = "02"
		elif split[3] == 'Mar':
			month = "03"
		elif split[3] == 'Apr':
			month = "04"
		elif split[3] == 'May':
			month = "05"
		elif split[3] == 'Jun':
			month = "06"
		elif split[3] == 'Jul':
			month = "07"
		elif split[3] == 'Aug':
			month = "08"
		elif split[3] == 'Sep':
			month = "09"
		elif split[3] == 'Oct':
			month = "10"
		elif split[3] == 'Nov':
			month = "11"
		elif split[3] == 'Dec':
			month = "12"

		sub_dir = split[8] 
		this_dir = os.path.join(to_dir, sub_dir)
		if os.path.isdir(this_dir) is False:
			os.makedirs(this_dir)

		timestamp = split[7].replace(':', '')
		new_file = split[8] + "-" + month + "-" + split[5] + "_" + timestamp + "" + file_ext
		print "Move " + new_file + ". To " + this_dir
		os.rename(file, new_file)
		shutil.move(new_file, this_dir)

