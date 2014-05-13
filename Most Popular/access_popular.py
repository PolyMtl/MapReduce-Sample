#!/usr/bin/python
import sys

maxCount = 0
maxPath = None

for line in sys.stdin:

	if line.endswith(" start\n"):
   		continue

   	try:	
		data = line.split("\t")
		link, count = data

		if float(maxCount) < float(count):
			maxPath = link
			maxCount = count
	except:
		continue

print "{0}\t{1}".format(maxPath, maxCount)