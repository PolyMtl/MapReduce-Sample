# Most Popular

## source
http://content.udacity-data.com/courses/ud617/access_log.gz

## shell
	cat access_log | ./access_mapper.py | sort | ./access_reducer.py | ./access_popular.py