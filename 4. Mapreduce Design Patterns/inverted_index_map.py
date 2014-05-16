#!/usr/bin/python
import sys
import re
import csv
def maper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    for line in reader:
    	id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
    	
    	body = re.split("[.!?:;\"()<>{}#$=_/ ,\-]", body)
        body = filter(None, body)

    	# print body
        for word in body:
        	word = word.lower();
        	if word and (word =="fantastic" or word == "fantastically"):
        		print "{0}\t{1}".format(word, id)
		
if __name__ == '__main__':
    maper()