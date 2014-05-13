#!/usr/bin/python
import sys

def maper():
	for line in sys.stdin:

		data = line.split(" ")
		try:
			link = data[:data[6].index("?")]

		except:
			link = data[6]
		
		try:
			link = link.replace("http://www.the-associates.co.uk", "")
		except:
			continue

		print "{0}\t1".format(link)
		
if __name__ == '__main__':
    maper()