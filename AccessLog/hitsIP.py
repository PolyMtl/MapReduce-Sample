#!/usr/bin/python
import sys

def maper():
	count = 0
	for line in sys.stdin:

		data = line.split(" ")
		ip = data[0]
	
		if ip == "10.99.99.186":
			count = count + 1

	print count
		
if __name__ == '__main__':
    maper()