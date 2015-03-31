import json
import numpy as np
import pyipinfodb
import time

ip_lookup = pyipinfodb.IPInfo('API_KEY_HERE')


f=open('ips.txt','r')
for line in f.readlines():
	print "Getting location for " + line 
	req=ip_lookup.get_city(line)
	time.sleep(0.5)
	srclong=float(req['longitude']); srclat=float(req['latitude'])
	with open('geo.txt', 'ab') as geo:
		geo.write(req['longitude'] + ',' + req['latitude']+'\n')

