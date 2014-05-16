#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    count = 0
    total = 0

    for line in reader:
        
        date = line[0]
        price = float(line[1])
        
        
        total += price
        count += 1

    print total 
    print count

# This function allows you to test the mapper with the provided test string
def main():
    import StringIO
    mapper()

main()
