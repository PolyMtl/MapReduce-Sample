#!/usr/bin/python
import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	oldKey = None
	indexList = []


	for line in reader:
		try:
			newKey, index = line
			if oldKey and oldKey != newKey:
				print "{0}\t{1} - {2}".format(oldKey, indexList, len(indexList))
				indexList = []
		
			oldKey = newKey
			# totalCount += float(count)
			indexList.append(index)

		except:
			continue



	if oldKey != None:
		print "{0}\t{1} - {2}".format(oldKey, indexList, len(indexList))

if __name__ == '__main__':
    reducer()