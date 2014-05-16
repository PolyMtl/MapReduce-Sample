#!/usr/bin/python

import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    total = count = 0

    for line in reader:
        
        date = line[0]
        price = float(line[4])
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

        if weekday != 6:
            continue
        
        total += price
        count += 1

    print total / count

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    mapper()

main()
