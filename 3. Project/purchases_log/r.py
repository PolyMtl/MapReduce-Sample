#!/usr/bin/python
import sys

def reducer():
	oldLoc = None
	oldName = ""
	maxPrice = 0

	for line in sys.stdin:

		data = line.split("\t")
		newLoc, name, price = data
		

		if  oldLoc and oldLoc != newLoc:
			# print newKey + " start"
			print "{0}\t{1}\t{2}".format(oldLoc, oldName, maxPrice)
			maxPrice = 0;

		oldLoc = newLoc
		oldName = name
		# totalCount += float(count)

		if float(maxPrice) < float(price):
			maxPrice = price

	if oldLoc != None:
		print "{0}\t{1}\t{2}".format(newLoc, oldName, maxPrice)

if __name__ == '__main__':
    reducer()