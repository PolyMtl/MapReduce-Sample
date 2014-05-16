#!/usr/bin/python

import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    oldDate = None
    total = 0

    for line in reader:
        
        date = line[0]
        price = float(line[4])
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

        if weekday != 6:
            continue
        
        if oldDate and oldDate != date:
            print "{0}\t{1}".format(oldDate, total)
            total = 0

        total += price
        oldDate = date

    print "{0}\t{1}".format(oldDate, total)

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    mapper()

main()
