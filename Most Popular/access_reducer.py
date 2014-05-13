#!/usr/bin/python
import sys

def reducer():
	oldKey = None
	totalCount = 0

	for line in sys.stdin:

		data = line.split("\t")
		newKey, count = data

		if oldKey and oldKey != newKey:
			# print newKey + " start"
			print "{0}\t{1}".format(oldKey, totalCount)
			totalCount = 0;

		oldKey = newKey
		totalCount += float(count)

	if oldKey != None:
		print "{0}\t{1}".format(oldKey, totalCount)

if __name__ == '__main__':
    reducer()