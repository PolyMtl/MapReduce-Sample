
# Purchases log
http://content.udacity-data.com/courses/ud617/purchases.txt.gz

## Sales per Category & Total Sales
	cat purchases.txt | ./map.py | sort | ./reduce.py > data.log
	
## Highest Sale
	cat purchases.txt | ./m.py | sort  | ./r.py > data.log 
 

 
	
---------

# Access log
http://content.udacity-data.com/courses/ud617/access_log.gz

## Hits to Page
	cat access_log | ./access_mapper.py | sort | ./access_reducer.py > data.log

## Hits from IP
	cat access_log | ./hitsIP.py 

## Most Popular
	cat access_log | ./access_mapper.py | sort | ./access_reducer.py | ./access_popular.py