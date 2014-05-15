#!/usr/bin/python
import sys

def maper():
	for line in sys.stdin:

		data = line.split("\t")

		# 2012-01-01	09:05	Austin	Health and Beauty	483.1	Visa
		date, time, loc, name, price, card = data
		
		print "{0}\t{1}".format(name, price)
		
if __name__ == '__main__':
    maper()