import json
import numpy as np
import pyipinfodb
import time

ip_lookup = pyipinfodb.IPInfo('API_KEY_HERE')


with open('ips.txt','r') as f:
	for line in f.readlines():
		print "Getting location for %s" % line 
		req=ip_lookup.get_city(line)
		time.sleep(0.5)
		with open('geo.txt', 'ab') as geo:
			geo.write('{},{}\n'.format(req['longitude'], req['latitude']))

