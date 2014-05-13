#!/usr/bin/python
import sys
# def maper():
for line in sys.stdin:
	# data = line[53:].split(" ")[0]
	# print data +"\t1"

	data = line.split(" ")
	# print data[6]
	try:
		link = data[:data[6].index("?")]
	 # +"\t1"
	except:
		link = data[6]
		 

	# print link
	print "{0}\t1".format(link)